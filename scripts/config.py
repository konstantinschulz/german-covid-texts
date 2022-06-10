import glob
import os.path


class Config:
    root_dir: str = os.getcwd() if glob.glob("LICENSE") else os.path.abspath("..")
    data_dir: str = os.path.join(root_dir, "data")
    sources_dir: str = os.path.join(data_dir, "sources")
    plain_text_dir: str = os.path.join(sources_dir, "plain_text")
    tok_dir: str = os.path.join(sources_dir, "tok")
    twitter_supplement_dir: str = os.path.join(data_dir, "supplements", "twitter_corpus_tokenized")
    data_raw_dir: str = os.path.join(sources_dir, "raw")
    docs_dir: str = os.path.join(root_dir, "docs")
    docs_src_dir: str = os.path.join(docs_dir, "src")
    encoding: str = "utf8"
    sample_raw_dir: str = os.path.join(data_raw_dir, "sample")
    sample_tok_dir: str = os.path.join(tok_dir, "sample")
    sample_tok_uncleaned_dir: str = os.path.join(sample_tok_dir, "uncleaned")
    sample_txt_dir: str = os.path.join(plain_text_dir, "sample")
    twitter_frequency_file_path: str = os.path.join(twitter_supplement_dir, "De.Freq.2.txt")
    twitter_word_probabilities_path: str = os.path.join(twitter_supplement_dir, "word_probabilities_descending.txt.gz")
