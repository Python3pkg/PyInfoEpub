#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST TEMPLATE CLI
----------------------------------

Tests a specific template
"""

import unittest

from pyinfoepub.templates.cli import TemplateCLI

class TemplateCliTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #self.main_parser = Parser(self.opf_content, deprecated=False)
        pass

    def test_init_content_keys_uppercase(self):
        content_test = {'key1':1, 'key2':2}
        expected = {'KEY1':1, 'KEY2':2}
        
        tcli = TemplateCLI(content=content_test)
        self.assertDictEqual(tcli.content, expected)
 
    def test_extract_placeholders(self):
        TEMPLATE = """{{PLACEHOLDER_1}} and {{PLACEHOLDER_2}} {NOT_PLACEHOLDER} some text"""
        
        tcli = TemplateCLI(content={})
        
        placeholders = tcli.extract_placeholders(TEMPLATE)
        self.assertEqual(placeholders,['{{PLACEHOLDER_1}}', '{{PLACEHOLDER_2}}'] )

    def test_render_separators(self):
        TEMPLATE = """{SEP_LINE} and some other {SEP_LINE}"""
        
        tcli = TemplateCLI(content={})
        tcli.tpl = TEMPLATE
        tcli.render_separators()
        
        self.assertNotEqual(tcli.tpl, TEMPLATE)
 
    def tearDown(self):
        pass

    
    
def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
