# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:56:52 2021

@author: Steven


E:\01_imageSet\04\src\01\001.jpg
E:\01_imageSet\04\src\01\002.jpg
E:\01_imageSet\04\src\01\003.jpg
...
E:\01_imageSet\04\src\02\001.jpg
E:\01_imageSet\04\src\02\002.jpg
...


----- change to:
    
E:\01_imageSet\04\target\01\01_001.jpg
E:\01_imageSet\04\target\01\01_002.jpg
E:\01_imageSet\04\target\01\01_003.jpg
...
E:\01_imageSet\04\target\02\02_001.jpg
E:\01_imageSet\04\target\02\02_002.jpg
...



"""



from os import walk
from os.path import join
import os
import shutil


mypath = r"E:\01_imageSet\04" #資料夾目錄


dir_path_src=join(mypath,"src")
dir_path_tar=join(mypath,"target")

if not os.path.isdir(dir_path_tar):
    os.mkdir(dir_path_tar)


for root, dirs, files in walk(dir_path_src):
    for dir_n in dirs:
        dir_path_result = join(dir_path_src,dir_n)
        allFileList = os.listdir(dir_path_result)   
        
        for file in allFileList:
            if(file.find(".jpg") != -1):
                root_split=dir_path_result.split('\\')
                
                if not os.path.isdir(dir_path_tar + "\\"+root_split[-1]):
                    os.mkdir(dir_path_tar + "\\"+root_split[-1])
                src_path =  join(dir_path_result,file)
                change_path = dir_path_tar + "\\"+root_split[-1]+"\\"+root_split[-1]+"_"+file
                print("change_fullpath: "+change_path)
                shutil.copyfile(src_path, change_path)
                                        




