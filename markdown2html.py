#!/usr/bin/python3
"""
Takes cmd arguments
First argument is the name of the Markdown file
Second argument is the output file name
If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesnt exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0
"""
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html')
        sys.exit(1)

    try:
        readme = open(sys.argv[1])
    except FileNotFoundError:
        sys.stderr.write(f'Missing {sys.argv[1]}')
        sys.exit(1)

    sys.exit(0)