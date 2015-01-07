# -*- coding: utf-8 -*-

import argparse
import sys

parser = argparse.ArgumentParser(prog="PyInfoEpub", description='Extracts information from an epub file.')
parser.add_argument('epub_file', metavar='file.epub', type=argparse.FileType('r'), default=sys.stdin, help='target epub file')
parser.add_argument('--version', action='version', version='%(prog)s 0.2')

args = parser.parse_args()

with args.epub_file as epub_file:
    print(epub_file.readlines())