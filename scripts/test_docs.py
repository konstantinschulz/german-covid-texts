import glob
import os.path
import re
import unittest

from config import Config


class DocsTestCase(unittest.TestCase):
    def test_links_internal(self):
        """Checks whether all pointers within the repository are working correctly."""
        for file_path in glob.glob(Config.docs_src_dir + '/**/*.md', recursive=True):
            with open(file_path) as f:
                content: str = f.read()
                # find all indices where a link follows
                start_indices: list[int] = [m.start() for m in re.finditer(r']\(', content)]
                start_indices.append(len(content) - 1)
                for i in range(len(start_indices) - 1):
                    opening_bracket_idx: int = start_indices[i] + 1
                    closing_bracket_idx: int = content.find(")", opening_bracket_idx, start_indices[i + 1])
                    link: str = content[opening_bracket_idx + 1:closing_bracket_idx]
                    # do not check external links
                    if link.startswith("http"):
                        continue
                    base_dir: str = os.path.dirname(file_path)
                    target_path: str = os.path.join(base_dir, link)
                    # verify that the target path points to a valid, existing file or folder
                    self.assertTrue(os.path.exists(target_path), msg=f"Dead link: {target_path} in file {file_path}")


if __name__ == '__main__':
    unittest.main()
