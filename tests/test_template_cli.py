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
        template = """{{PLACEHOLDER_1}} and {{PLACEHOLDER_2}} {NOT_PLACEHOLDER} some text"""
        
        tcli = TemplateCLI({}, template)
        
        placeholders = tcli.extract_placeholders(template)
        self.assertEqual(placeholders,['{{PLACEHOLDER_1}}', '{{PLACEHOLDER_2}}'] )

    def test_render_separators(self):
        template = """{SEP_LINE} and some other {SEP_LINE}"""
        
        tcli = TemplateCLI({}, template)
        tcli.render_separators()

    def test_render_single_elements(self):
        template = """{{SINGLE_ELEM1}}|Lorem|{{SINGLE_ELEM2}}|Ipsum|{{COMPLEX_ELEM|m}}"""
        out_template = """Test|Lorem|Test|Ipsum|{{COMPLEX_ELEM|m}}"""
        
        input_content = {'single_elem1': 'Test', 'single_elem2': 'Test'}
        
        tcli = TemplateCLI(input_content, template)
        tcli.render_single_elements()
        
        self.assertEqual(tcli.tpl, out_template)

    def test_render_single_elements_missing_key(self):
        template = """{{SINGLE_ELEM1}}|Lorem|{{MISING_ELEM}}|Ipsum|{{COMPLEX_ELEM|m}}"""
        out_template = """Test|Lorem||Ipsum|{{COMPLEX_ELEM|m}}"""
        
        input_content = {'single_elem1': 'Test'}
        
        tcli = TemplateCLI(input_content, template)
        tcli.render_single_elements()
        
        self.assertEqual(tcli.tpl, out_template)

    def test_render_list_elements(self):
        template = """REPLACE REPLACE REPLACE Lorem Ipsum REPLACE"""
        out_template = """one, two one, two one, two Lorem Ipsum one, two"""
        
        cph = "REPLACE"
        replacement = ["one", "two"]
        
        tcli = TemplateCLI({}, template)
        tcli.render_list_elements(cph, replacement)

        self.assertEqual(tcli.tpl, out_template)

    def test_render_custom_identifiers(self):
        template = """REPLACE"""
        out_template = """(Scheme1:Ident1) some_id\n(Scheme2:Ident2) some_id"""
        
        cph = "REPLACE"
        replacement = [
            {'scheme':'Scheme1', 'ident':'Ident1', 'id':'some_id'},
            {'scheme':'Scheme2', 'ident':'Ident2', 'id':'some_id'}
        ]
        
        tcli = TemplateCLI({}, template)
        tcli.render_custom_identifiers(cph, replacement)

        self.assertEqual(tcli.tpl, out_template)

    def tearDown(self):
        pass

    
    
def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
