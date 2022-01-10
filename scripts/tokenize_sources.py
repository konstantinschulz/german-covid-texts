import os

import nltk as nltk
from tika import parser
from tqdm import tqdm

from config import Config


def tokenize():
    """ Splits raw source data into sentences and tokens. """
    for file in tqdm(os.listdir(Config.sample_raw_dir)):
        raw: dict = parser.from_file(os.path.join(Config.sample_raw_dir, file), service="text", xmlContent=True)
        content: str = raw['content'].replace("\n", " ").strip()
        language: str = "german"
        sent_tok: list[list[str]] = []
        for sent in nltk.sent_tokenize(content, language=language):
            sent_tok.append(nltk.word_tokenize(sent, language=language))
        # change file extension to .txt
        target_path: str = os.path.join(Config.sample_tok_dir, os.path.splitext(file)[0] + ".txt")
        with open(target_path, "w+") as f:
            f.write("\n".join([" ".join(x) for x in sent_tok]))


tokenize()
