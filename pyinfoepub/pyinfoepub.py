# -*- coding: utf-8 -*-

import argparse
import sys

from lib.info_epub import PyInfoEpub

parser = argparse.ArgumentParser(prog="PyInfoEpub", description='Extracts information from an epub file.')
parser.add_argument('epub_file', metavar='file.epub', type=argparse.FileType('r'), default=sys.stdin, help='target epub file')
parser.add_argument('--version', action='version', version='%(prog)s 0.2')

args = parser.parse_args()

pyob = PyInfoEpub(args.epub_file.name)
pyob.get_info()