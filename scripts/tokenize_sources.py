# -*- coding: utf-8 -*-

import os
import re

import nltk as nltk
from tika import parser
from tqdm import tqdm
import json

from config import Config


def get_text_from_json(file) -> str:
    """ Extracts plain text from a JSON file. """
    json_file = os.path.join(Config.sample_raw_dir, file)
    content: str = ""
    with open(json_file, 'r', encoding="utf8") as f:
        data: dict = json.load(f)
        for section in data["sections"]:
            content += " " + section["sectionTitle"]
            content += section["text"]
    return content


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
