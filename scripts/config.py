import glob
import os.path


class Config:
    root_dir: str = os.getcwd() if glob.glob("LICENSE") else os.path.abspath("..")
    data_dir: str = os.path.join(root_dir, "data")
    sources_dir: str = os.path.join(data_dir, "sources")
    plain_text_dir: str = os.path.join(sources_dir, "plain_text")
    tok_dir: str = os.path.join(sources_dir, "tok")
    data_raw_dir: str = os.path.join(sources_dir, "raw")
    docs_dir: str = os.path.join(root_dir, "docs")
    docs_src_dir: str = os.path.join(docs_dir, "src")
    encoding: str = "utf8"
    sample_raw_dir: str = os.path.join(data_raw_dir, "sample")
    sample_tok_dir: str = os.path.join(tok_dir, "sample")
    sample_txt_dir: str = os.path.join(plain_text_dir, "sample")
