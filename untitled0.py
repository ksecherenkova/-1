# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:54:26 2018

@author: ksu
"""

import re
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input',
                        metavar='<path to file>', required=True)
parser.add_argument('--output',
                        metavar='<path to file>')
parser.add_argument('--tags',
                        metavar='<options>', nargs='+')
                        

args = parser.parse_args()
path_to_file = args.input
path_out = args.output
tag = args.tags
search_tags = ('locus', 'definition', 'accession', 'source', 'title')

pattern = re.compile(r'''LOCUS(?P<locus>.*?)       
                        DEFINITION(?P<definition>.*?)      
                        ACCESSION(?P<accession>.*?) 
                        SOURCE(?P<source>.*?)        
                        TITLE(?P<title>[^(JOURNAL)]*?
                        ''')
strip = re.compile(r'''\s+''')
file = open(path_to_file, 'r') 
file = file.read()
found = re.finditer(pattern, file)
result = []


for each in found:
    result.append([re.sub(strip, ' ', each.group(i).strip()) for i in search_tags])
file_out = open(path_out, 'w')
file_out = csv.writer(file_out)

file_out.writerow(search_tags)
for each in result:
    file_out.writerow(i)

