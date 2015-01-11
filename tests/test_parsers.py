#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST PARSERS
----------------------------------

Tests for parsers module
"""

import unittest
from xml.dom import minidom

from pyinfoepub.src.parsers_epub import *

# TESTS ARE BASED ON THIS SAMPLE
OPF_SAMPLE_FILE = './samples/content.opf'

class ParsersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(OPF_SAMPLE_FILE, 'r') as f:
            cls.opf_content = minidom.parseString(f.read())
    
    def setUp(self):
        self.main_parser = Parser(self.opf_content, deprecated=False)

    # MAIN PARSER TESTS
    def test_main_parser_change(self):
        def dummy_parser():
            pass
        self.main_parser.change(dummy_parser)
        self.assertIs(dummy_parser, self.main_parser.parser)

    def test_main_parser_change_return_self(self):
        def dummy_parser():
            pass
        returned = self.main_parser.change(dummy_parser)
        self.assertIsInstance(returned, Parser)
        
    def test_main_parser_parse_method(self):
        def dummy_parser(obj):
            return obj
        self.main_parser.change(dummy_parser)
        returned = self.main_parser.parse()
        self.assertIs(returned, self.main_parser)

    def test_main_parser_get_elem_deprecated_flag_off(self):
        self.main_parser.deprecated_flag = False
        node_list = self.main_parser.get_elem('rights')
        self.assertEqual(node_list.length, 1)

    def test_main_parser_get_elem_deprecated_flag_on(self):
        self.main_parser.deprecated_flag = True
        node_list = self.main_parser.get_elem('rights')
        self.assertEqual(node_list.length, 0)

    # ParserBookTitle
    def test_parser_book_title_should_return_string(self):
        returned = self.main_parser.change(ParserBookTitle).parse()
        self.assertEqual(returned, "Metamorphosis")

    # ParserCreator
    def test_parser_creator_should_return_list(self):
        returned = self.main_parser.change(ParserCreator).parse()
        self.assertIsInstance(returned, list)
        self.assertIsInstance(returned[0], str)
        self.assertEqual(returned[0], 'Franz Kafka')

    def test_parser_creator_return_empty_list_for_noresults(self):
        self.set_empty_content()
        returned = self.main_parser.change(ParserCreator).parse()
        self.assertEqual(returned, [])
        self.revert_valid_content()

    # ParserSubject
    def test_parser_subject_should_return_list(self):
        returned = self.main_parser.change(ParserSubject).parse()
        self.assertIsInstance(returned, list)
        self.assertIsInstance(returned[0], str)
        self.assertEqual(returned[0], 'Psychological fiction')
        
    def test_parser_subject_return_empty_list_for_no_results(self):
        self.set_empty_content()
        returned = self.main_parser.change(ParserSubject).parse()
        self.assertEqual(returned, [])
        self.revert_valid_content()

    def test_parser_subject(self):
        pass

    def tearDown(self):
        pass


    # Helpers
    def set_empty_content(self):
        """Setup an empty xml content for the main parser"""
        self.main_parser.content = minidom.parseString("<?xml version='1.0' encoding='UTF-8'?><package></package>")

    def revert_valid_content(self):
        self.main_parser.content = self.opf_content




def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

def main():
    buildTestSuite()
    unittest.main()
    
if __name__ == "__main__":
    main()