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


def remove_hyphenation(text: str) -> str:
    """ Removes hyphenation from the text which was introduced by line breaks in print publications. """
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
    lines = text.split(" ")
    index = 0
    text_tokenized = []
    skip_next = False
    for word in lines:
        if word.endswith("-"):
            next_word = lines[index + 1]
            word_rm = word[:-1]
            if next_word[0] != "und" and next_word[0] != "oder":
                tags = tagger.tag_text(word_rm + next_word)
                lemmatize = treetaggerwrapper.make_tags(tags)
                lemma = lemmatize[0][2]
                if next_word[0].islower() and duden.search(lemma) != []:
                    word = word_rm + next_word
                    text_tokenized.append(word)
                    skip_next = True
                elif next_word[0].islower() and duden.search(lemma) == []:
                    if check_last_char(word_rm, next_word):
                        word = word_rm + next_word
                        text_tokenized.append(word)
                        skip_next = True
                    else:
                        if skip_next:
                            skip_next = False
                            index += 1
                            continue
                        text_tokenized.append(word)
                else:
                    if skip_next:
                        skip_next = False
                        index += 1
                        continue
                    text_tokenized.append(word)
            else:
                if skip_next:
                    skip_next = False
                    index += 1
                    continue
                text_tokenized.append(word)
            index += 1
        else:
            if skip_next:
                skip_next = False
                index += 1
                continue
            text_tokenized.append(word)
            index += 1
            
    return " ".join(text_tokenized)

def check_last_char(first_word, second_word):
    if second_word[-1] == "-":
        second_word = second_word[:-1]
    word = first_word + second_word
    print(word)
    fugenelement = False
    if duden.search(word[:-1]) != [] and word[-1] == "s":
        fugenelement = True
    return fugenelement


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
