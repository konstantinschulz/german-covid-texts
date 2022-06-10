# -*- coding: utf-8 -*-
import tempfile
from clint.textui import progress
import gzip
import os
import re
from typing import Counter
import wordninja
import duden
import nltk as nltk
import patoolib
import requests
import treetaggerwrapper
from tika import parser
from tqdm import tqdm
import json

from config import Config


def add_word_to_token_list(word: str, text_tokenized: list[str], index: int) -> tuple[list[str], int]:
    """ Adds a new token to the list and moves the index to the next word. """
    text_tokenized.append(word)
    return text_tokenized, index + 1


def check_last_char(first_word, second_word):
    """ Checks for linking elements at the end of a word. """
    if second_word[-1] == "-":
        second_word = second_word[:-1]
    word = first_word + second_word
    fugenelement = False
    if has_dict_entry(word[:-1]) and word[-1] == "s":
        fugenelement = True
    return fugenelement


def combine_words(word_rm: str, next_word: str, text_tokenized: list[str]) -> tuple[str, list[str], bool]:
    """ Combines two words that were separated by a hyphen to form a new one. """
    word: str = word_rm + next_word
    text_tokenized.append(word)
    return word, text_tokenized, True


def get_text_from_json(file_path: str) -> str:
    """ Extracts plain text from a JSON file. """
    content: str = ""
    with open(file_path, 'r', encoding="utf8") as f:
        data: dict = json.load(f)
        for section in data["sections"]:
            content += " " + section["sectionTitle"]
            content += section["text"]
    return content


def has_dict_entry(word: str) -> bool:
    """ Checks whether a word is contained in a dictionary. """
    word_lower = word[0].lower() + word[1:]
    word_upper = word[0].upper() + word[1:]
    if duden.search(word_lower) != [] or duden.search(word_upper) != []:
        return True
    return False


def increase_index(index: int) -> tuple[int, bool]:
    """ Moves the index to the next word and resets the skip flag. """
    return index + 1, False


def make_probability_distribution():
    """ Creates a list of words ordered by probability of occurring in a corpus. """
    def download_file(url: str, twitter_supplement_dir: str):
        """ Downloads a RAR archive with a progress bar and extracts it. """
        # create a streamed GET request
        r: requests.Response = requests.get(url, stream=True)
        # create a temporary file to store the RAR data
        fd, path = tempfile.mkstemp()
        try:
            with open(fd, "wb") as f:
                # determine the overall size of the RAR archive
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            # extract the RAR; please note: binary for rar, unrar or 7z needs to be installed BEFORE running this script
            patoolib.extract_archive(path, outdir=twitter_supplement_dir)
        finally:
            # remove the temporary file with the RAR data
            os.remove(path)
    counter: Counter = Counter()
    if not os.path.exists(Config.twitter_word_probabilities_path):
        print("Downloading word frequency data for Twitter...")
        download_file("http://worldlex.lexique.org/files/De.Freq.2.rar", Config.twitter_supplement_dir)
        print("Building tokenizer...")
        with open(Config.twitter_frequency_file_path) as f:
            # shape: ['Word', 'BlogFreq', 'BlogFreqPm', 'BlogCD', 'BlogCDPc', 'TwitterFreq', 'TwitterFreqPm', 'TwitterCD', 'TwitterCDPc', 'NewsFreq', 'NewsFreqPm', 'NewsCD', 'NewsCDPc.']
            for idx, line in tqdm(enumerate(f.readlines()), total=1711608):
                if idx == 0:
                    continue
                values: list[str] = line.split("\t")
                counter.update({values[0]: float(values[5])})
    with gzip.open(Config.twitter_word_probabilities_path, mode="wt", encoding="utf-8") as f:
        f.write("\n".join([x[0] for x in counter.most_common()]))


def normalize_text(text: str) -> str:
    """ Removes additional whitespace and hyphenation. """
    # remove line breaks and trailing whitespace
    text = text.replace("\n", " ").strip()
    # remove tabs
    text = re.sub(r"\t", " ", text)
    # collapse duplicate whitespace into single whitespace
    text = re.sub(r" +", " ", text)
    # remove erroneous hyphenation
    text = remove_hyphenation(text)
    return text


def remove_hyphenation(text: str) -> str:
    """ Removes hyphenation from the text which was introduced by line breaks in print publications. """
    tagger: treetaggerwrapper.TreeTagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
    lines: list[str] = text.split(" ")
    index: int = 0
    text_tokenized: list[str] = []
    skip_next: bool = False
    url_markers: set[str] = {"http", "www", ".com", ".de", ".html", "/"}
    connectors: set[str] = {"und", "oder"}
    for word in lines:
        try:
            # exclude URLs
            if any(x for x in url_markers if x in word):
                text_tokenized.append(word)
                index, skip_next = increase_index(index)
                continue
            elif word.endswith("-"):
                next_word: str = lines[index + 1]
                word_rm: str = word[:-1]
                if next_word not in connectors:
                    tags: list[str] = tagger.tag_text(word_rm + next_word)
                    lemmatize: list[treetaggerwrapper.Tag] = treetaggerwrapper.make_tags(tags)
                    lemma: str = lemmatize[0][2]
                    if next_word[0].islower():
                        if has_dict_entry(lemma):
                            word, text_tokenized, skip_next = combine_words(word_rm, next_word, text_tokenized)
                        else:
                            if check_last_char(word_rm, next_word):
                                word, text_tokenized, skip_next = combine_words(word_rm, next_word, text_tokenized)
                            else:
                                if skip_next:
                                    index, skip_next = increase_index(index)
                                    continue
                                text_tokenized.append(word)
                    else:
                        if skip_next:
                            index, skip_next = increase_index(index)
                            continue
                        text_tokenized.append(word)
                else:
                    if skip_next:
                        index, skip_next = increase_index(index)
                        continue
                    text_tokenized.append(word)
                index += 1
            else:
                if skip_next:
                    index, skip_next = increase_index(index)
                    continue
                text_tokenized, index = add_word_to_token_list(word, text_tokenized, index)
        except:
            if skip_next:
                index, skip_next = increase_index(index)
                continue
            text_tokenized, index = add_word_to_token_list(word, text_tokenized, index)
    return " ".join(text_tokenized)


def tokenize() -> None:
    """ Splits raw source data into sentences and tokens. """
    print("Loading tokenizer...")
    lm: wordninja.LanguageModel = wordninja.LanguageModel(Config.twitter_word_probabilities_path)
    # add Umlauts and ß (German sharp S) to the allowed characters in a word
    wordninja._SPLIT_RE = re.compile("[^a-zA-Z0-9\u0080-\u00FF]+")
    print("Tokenizing input files...")
    for file in tqdm(os.listdir(Config.sample_raw_dir)):
        content: str
        file_path: str = os.path.join(Config.sample_raw_dir, file)
        # extract plain text from JSON files
        if ".json" in file:
            content = get_text_from_json(file_path)
        # extract plain text from non-JSON files
        else:
            raw: dict = parser.from_file(file_path, service="text", xmlContent=True)
            content = raw['content']
        content = normalize_text(content)
        # change file extension to .txt
        target_file_name: str = os.path.splitext(file)[0] + ".txt"
        target_path: str = os.path.join(Config.sample_txt_dir, target_file_name)
        with open(target_path, "w+", encoding=Config.encoding) as f:
            # write plain text to file
            f.write(content)
        language: str = "german"
        sent_tok: list[list[str]] = []
        # segmentation
        for sent in nltk.sent_tokenize(content, language=language):
            # tokenization
            sent_tok.append(nltk.word_tokenize(sent, language=language))
        # fix hashtag tokenization
        tokenize_hashtags(sent_tok, lm)
        target_path = os.path.join(Config.sample_tok_uncleaned_dir, target_file_name)
        with open(target_path, "w+", encoding=Config.encoding) as f:
            # write tokenized text to file
            f.write("\n".join([" ".join(x) for x in sent_tok]))


def tokenize_hashtags(sent_tok: list[list[str]], lm: wordninja.LanguageModel) -> list[list[str]]:
    """ Splits hashtags that are concatenations of multiple words into single tokens. """
    for st in sent_tok:
        try:
            idx: int = st.index("#")
            # search for hashtags
            while True:
                hashtag: str = st[idx + 1]
                # get new tokenization for the hashtag
                tokens: list[str] = lm.split(hashtag)
                if len(tokens) > 1:
                    st.remove(hashtag)
                    for i in range(len(tokens)):
                        idx += 1
                        # add the new tokens to the list
                        st.insert(idx + i, tokens[i])
                # this will throw ValueError if no more hashtags are present in the rest of the list
                idx = st.index("#", idx + 1)
        # no (more) hashtags present, skip the sentence
        except ValueError:
            continue


# make_probability_distribution()
tokenize()
