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

OPF_SAMPLE_FILE = './samples/content.opf'

class ParsersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(OPF_SAMPLE_FILE, 'r') as f:
            cls.opf_content = minidom.parseString(f.read())
    
    def setUp(self):
        self.main_parser = Parser(self.opf_content, deprecated=False)

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

    def test_get_elem_deprecated_flag_off(self):
        self.main_parser.deprecated_flag = False
        node_list = self.main_parser.get_elem('rights')
        self.assertEqual(node_list.length, 1)

    def test_get_elem_deprecated_flag_on(self):
        self.main_parser.deprecated_flag = True
        node_list = self.main_parser.get_elem('rights')
        self.assertEqual(node_list.length, 0)

    def tearDown(self):
        pass




def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

def main():
    buildTestSuite()
    unittest.main()
    
if __name__ == "__main__":
    main()