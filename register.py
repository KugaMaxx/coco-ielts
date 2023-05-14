import os, sys
import glob
import time
import platform
import numpy as np
import pandas as pd


dir = "./books"
clear = 'clear' if platform.system() == 'Linux' else 'cls'

books = os.listdir(dir)
books.sort()
print("输入要录入的词典（输入序号后回车）\n")
for b in books:
    print(f"{b}")
print()

idb = int(input()) - 1
os.system(clear)
if idb < 0 or idb >= len(books):
    sys.exit()
else:
    chaps_dir = os.path.join(dir, books[idb])
    chaps = os.listdir(chaps_dir)

chaps.sort()
print("输入要进入的章节（输入序号后回车）\n")
for c in chaps:
    print(f"{c}")
print()

idc = int(input()) - 1
os.system(clear)
if idc < 0 or idc >= len(chaps):
    sys.exit()
else:
    dict_dir = os.path.join(os.path.join(dir, books[idb]), chaps[idc])
    dicts = pd.read_csv(dict_dir, dtype={'word': str,
                                         'page': str,
                                         'time': int})
    
while 1:
    os.system(clear)
    print("录入新单词（退出请输入0）...")
    print("  单词: ", end="")
    new_word = input()
    if (new_word == '0'): break
    print("  页码: ", end="")
    new_page = input()
    dicts.loc[len(dicts.index)] = [new_word, new_page, 0]

os.system(clear)
print("\r储存结果中，请稍候", end="")
dicts.to_csv(dict_dir, index=False)
print("\r储存完毕，退出程序")

# st = time.time()
# dc = pd.read_csv('./stardict.csv', sep=',',
#                 dtype={'word': str,
#                         'phonetic': str,
#                         'definition': str,
#                         'translation': str,
#                         'pos': str,
#                         'collins': str,
#                         'oxford': str,
#                         'tag': str,
#                         'bnc': str,
#                         'frq': str,
#                         'exchange': str,
#                         'detail': str,
#                         'audio': str})


# print(time.time() - st)
