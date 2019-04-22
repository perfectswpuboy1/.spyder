# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyexcel

#通过字典方式储存即将写入xls文件的数据。

a_list_of_dictionaries = [
     {
         "Name": 'Adam',
         "Age": 28
     },
     {
         "Name": 'Beatrice',
         "Age": 29
     },
     {
         "Name": 'Ceri',
         "Age": 30
     },
     {
         "Name": 'Dean',
         "Age": 26
     }
 ]
#总共有四个人的年龄数据
pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls") #创建xls文件并写入字典内容