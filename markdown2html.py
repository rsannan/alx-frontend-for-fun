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
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            data = f.readlines()
            for line in data:
                if '#' in line:
                    words = line.split()
                    for word in words:
                        if word == '#':
                            sum += 1
                    final_word = f"<h{sum}> {}"

    except FileNotFoundError:
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)

    sys.exit(0)