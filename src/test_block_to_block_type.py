import unittest
from markdown_to_blocks import *

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading(self):
        markdown = "# Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")
        
        markdown = "## Subheading"
        self.assertEqual(block_to_block_type(markdown), "heading")
    
    def test_code(self):
        markdown = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(markdown), "code")
    
    def test_quote(self):
        markdown = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(markdown), "quote")
    
    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(markdown), "unordered_list")
        
        markdown = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(markdown), "unordered_list")
    
    def test_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(markdown), "ordered_list")
    
    def test_paragraph(self):
        markdown = "This is a paragraph."
        self.assertEqual(block_to_block_type(markdown), "paragraph")
        
        markdown = "This is a paragraph.\nWith multiple lines."
        self.assertEqual(block_to_block_type(markdown), "paragraph")

if __name__ == "__main__":
    unittest.main()