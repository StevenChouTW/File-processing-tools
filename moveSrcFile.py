# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:50:49 2021

@author: Steven


比較名稱

假設read\1-1\ 資料夾內, 有 +001.jpg影像
那我要去掉 '+' 符號後, 
將 src\1-1\ 資料夾內同名稱的檔案 001.jpg
複製到 result\1-1\ 內, 001.jpg



"""

import os
import shutil
from os.path import join


path = r"E:\test_file\read\1-1"
src=r"E:\test_file\src\1-1"
result=r"E:\test_file\result\1-1"

if not os.path.isdir(result):
    os.mkdir(result)

files = os.listdir(path)

for file in files:
    if(file.lower().endswith('jpg')):
        if '+' in file[0]:
            srcFileName= file.replace('+', '')
            if( os.path.isfile(join(src, srcFileName) ) ):
                shutil.copyfile(join(src, srcFileName) \
                                , join(result, srcFileName))
            else:
                print( join(src, srcFileName) , "is not exist!")
        