# -*- coding: utf-8 -*-

import argparse
import sys

from src.info_epub import PyInfoEpub
from src.template_cli import TemplateCLI

parser = argparse.ArgumentParser(prog="PyInfoEpub", description='Extracts information from an epub file.')
parser.add_argument('epub_file', metavar='file.epub', type=argparse.FileType('r'), default=sys.stdin, help='target epub file')
parser.add_argument('--version', action='version', version='%(prog)s 0.2')

args = parser.parse_args()

pyob = PyInfoEpub(args.epub_file.name)
extracted_info = pyob.get_info()


tob = TemplateCLI(extracted_info)
tob.render()