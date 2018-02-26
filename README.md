# Finding articles by keywords

###### *Each found gene is formed according to the rules [click](https://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html)*

## Input

* File with GenBank search results 
* Keywords

## A little about libraries

###### First you need to install...

1. re
2. csv
3. argparse

import it all ~~gently~~

- [x] import re 
- [x] import csv 
- [x] import argparse 

## Valid tags
###### Search will be performed by tags

- locus
- definition
- accession
- source
- title

```
search_tags = ('locus', 'definition', 'accession', 'source', 'title')
```

## Output

The program stores the result of the search in a **_csv-file_** (file_out)
