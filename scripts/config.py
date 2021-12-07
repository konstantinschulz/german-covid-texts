import glob
import os.path


class Config:
    root_dir: str = os.getcwd() if glob.glob("LICENSE") else os.path.abspath("..")
    docs_dir: str = os.path.join(root_dir, "docs")
    docs_src_dir: str = os.path.join(docs_dir, "src")
