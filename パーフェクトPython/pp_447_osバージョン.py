#!/usr/bin/env python

import os

# カレント/親への相対パスを返却する。
print(os.path.curdir)
print(os.path.pardir)

# 親ディレクトリの絶対パスを返却する。
print(os.path.abspath(os.path.pardir))

# ベースネームを返却
print(os.path.basename('C:\github\study\hogehoge.py'))
