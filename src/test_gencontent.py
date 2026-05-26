import unittest
from gencontent import extract_title

class test_gencontent(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal...
"""
        result = extract_title(md)
        expected = "Tolkien Fan Club"
        self.assertEqual(result, expected)
    
    def test_extract_title_ignores_h6(self):
        with self.assertRaises(Exception):
            extract_title("###### Not a title")

    def test_not_first_line_extract_title(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)

# Tolkien Fan Club

Here's the deal...
"""

        result = extract_title(md)
        expected = "Tolkien Fan Club"
        self.assertEqual(result, expected)
    
    def test_ignore_h2_extract_title(self):
        md = """
![JRR Tolkien sitting](/images/tolkien.png)

# Tolkien Fan Club

Here's the deal...

## Tolkien Fan Club2
"""

        result = extract_title(md)
        expected = "Tolkien Fan Club"
        self.assertEqual(result, expected)