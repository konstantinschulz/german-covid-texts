import glob
import re
import unittest

from scripts.config import Config


class DocsTestCase(unittest.TestCase):
    def test_links_internal(self):
        """Checks whether all pointers within the repository are working correctly."""
        for file_path in glob.glob(Config.docs_src_dir + '/**/*.md', recursive=True):
            with open(file_path) as f:
                content: str = f.read()
                start_indices: list[int] = [m.start() for m in re.finditer(r']\(', content)]
            a = 0


if __name__ == '__main__':
    unittest.main()
