#!/usr/bin/env python
"""It is a Python command-line tool which reads in tagging data and randomly splits it into training, development, and test data"""

import argparse
import random 
from typing import Iterator, List

def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines


def main(args: argparse.Namespace) -> None:
    text = list(read_tags(args.input))
    random.seed(args.seed)
    random.shuffle(text)
    train = text[:8758]
    dev = text[8759:9853]
    test = text[9854:]


    with open(args.train, 'w') as filehandle:
        for listitem in train:
            filehandle.write('%s\n' % listitem)
    
    with open(args.dev, 'w') as filehandle:
        for listitem in dev:
            filehandle.write('%s\n' % listitem)

    with open(args.test, 'w') as filehandle:
        for listitem in test:
            filehandle.write('%s\n' % listitem)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--seed", type=int, required=True
    )
    parser.add_argument(
        "input"
    )
    parser.add_argument(
        "train"
    )
    parser.add_argument(
        "dev"
    )
    parser.add_argument(
        "test"
    )
    main(parser.parse_args())
