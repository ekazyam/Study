#!/usr/bin/env python

import sys
import os
import stagger
from stagger import id3


def main(args=sys.argv[1:]):
    fpath = args[0]

    # stagger.read_tag関数でmp3ファイルタグから情報を読み込む
    tag = stagger.read_tag(fpath)

    print(tag)

    print(tag.title)

    print(tag.album)

if __name__ == '__main__':
    main()
