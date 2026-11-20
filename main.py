#!/usr/bin/env python3
"""news-image-20261120 entry: the world's news of Friday 20 November 2026,
summed up in one image.

Writes the image to /output/entry.png. Deterministic: the output is a
byte-for-byte copy of entry.png shipped in this repository, so two runs
produce byte-identical output. Python 3.13, standard library only.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
