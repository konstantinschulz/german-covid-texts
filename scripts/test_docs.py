import glob
import os.path
import re
import unittest

from config import Config


class DocsTestCase(unittest.TestCase):

    @staticmethod
    def check_named_anchor(self: unittest.TestCase, file_path: str, link: str):
        """ Verifies that a link points to a valid named anchor within the given document. """
        # named anchors must start with a hashtag, followed by whitespace, and end with a line break
        named_anchor: str = f"{link[:1]} {link[1:]}\n"
        with open(file_path) as f:
            content: str = f.read()
            self.assertIn(named_anchor, content.lower())

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
                    elif "#" in link:
                        DocsTestCase.check_named_anchor(self, file_path, link)
                        continue
                    base_dir: str = os.path.dirname(file_path)
                    target_path: str = os.path.join(base_dir, link)
                    # verify that the target path points to a valid, existing file or folder
                    self.assertTrue(os.path.exists(target_path), msg=f"Dead link: {target_path} in file {file_path}")


if __name__ == '__main__':
    unittest.main()
