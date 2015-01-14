#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST INFO EPUB
----------------------------------

Tests for info_epub module
"""

from io import BytesIO
import unittest

from infoepub import *  # NOQA

# TESTS ARE BASED ON THIS SAMPLE
EPUB_SAMPLE_FILE = './samples/Franz Kafka - Metamorphosis.epub'


class InfoEpubTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.info_epub = PyInfoEpub(EPUB_SAMPLE_FILE)

    def test_info_epub_after_init(self):
        self.assertEqual(self.info_epub.epub_filename, EPUB_SAMPLE_FILE)
        self.assertEqual(
            self.info_epub.epub_content, {}, 'Content should be an empty dict.')
        self.assertEqual(self.info_epub.opf, None, 'OPF should be None.')
        self.assertFalse(
            self.info_epub.deprecated_flag, 'Deprecated flag should be False.')

    def test_unzip_should_produce_dict_of_bytes(self):
        self.info_epub.unzip()
        for k, v in self.info_epub.epub_content.items():
            self.assertIsInstance(v, BytesIO)

    def test_unzip_invalid_filename(self):
        self.invalid_info_epub = PyInfoEpub('invalid.epub')
        self.assertRaises(FileNotFoundError, self.invalid_info_epub.unzip)

    def setUp(self):
        pass

    def tearDown(self):
        pass


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
