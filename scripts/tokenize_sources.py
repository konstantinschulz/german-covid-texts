import os
import re

import nltk as nltk
from tika import parser
from tqdm import tqdm

from config import Config


def tokenize():
    """ Splits raw source data into sentences and tokens. """
    for file in tqdm(os.listdir(Config.sample_raw_dir)):
        raw: dict = parser.from_file(os.path.join(Config.sample_raw_dir, file), service="text", xmlContent=True)
        # remove line breaks and trailing whitespace
        content: str = raw['content'].replace("\n", " ").strip()
        # remove tabs
        content = re.sub(r"\t", " ", content)
        # collapse duplicate whitespace into single whitespace
        content = re.sub(r" +", " ", content)
        # change file extension to .txt
        target_file_name: str = os.path.splitext(file)[0] + ".txt"
        target_path: str = os.path.join(Config.sample_txt_dir, target_file_name)
        with open(target_path, "w+") as f:
            # write plain text to file
            f.write(content)
        language: str = "german"
        sent_tok: list[list[str]] = []
        for sent in nltk.sent_tokenize(content, language=language):
            sent_tok.append(nltk.word_tokenize(sent, language=language))
        target_path = os.path.join(Config.sample_tok_dir, target_file_name)
        with open(target_path, "w+") as f:
            # write tokenized text to file
            f.write("\n".join([" ".join(x) for x in sent_tok]))


tokenize()
