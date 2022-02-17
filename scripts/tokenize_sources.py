# -*- coding: utf-8 -*-

import os
import re

import duden
import nltk as nltk
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
    json_file_path: str = os.path.join(Config.sample_raw_dir, file_path)
    content: str = ""
    with open(json_file_path, 'r', encoding="utf8") as f:
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
    for file in tqdm(os.listdir(Config.sample_raw_dir)):
        content: str
        if ".json" in file:
            content = get_text_from_json(file)
        else:
            raw: dict = parser.from_file(os.path.join(Config.sample_raw_dir, file), service="text", xmlContent=True)
            content = raw['content']
        # remove line breaks and trailing whitespace
        content = content.replace("\n", " ").strip()
        # remove tabs
        content = re.sub(r"\t", " ", content)
        # collapse duplicate whitespace into single whitespace
        content = re.sub(r" +", " ", content)
        # remove erroneous hyphenation
        content = remove_hyphenation(content)
        # change file extension to .txt
        target_file_name: str = os.path.splitext(file)[0] + ".txt"
        target_path: str = os.path.join(Config.sample_txt_dir, target_file_name)
        with open(target_path, "w+", encoding=Config.encoding) as f:
            # write plain text to file
            f.write(content)
        language: str = "german"
        sent_tok: list[list[str]] = []
        for sent in nltk.sent_tokenize(content, language=language):
            sent_tok.append(nltk.word_tokenize(sent, language=language))
        target_path = os.path.join(Config.sample_tok_dir, target_file_name)
        with open(target_path, "w+", encoding=Config.encoding) as f:
            # write tokenized text to file
            f.write("\n".join([" ".join(x) for x in sent_tok]))


tokenize()
