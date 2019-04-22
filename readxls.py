# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:04:54 2019

@author: x230
"""

import pyexcel as p

records = p.iget_records(file_name="your_file.xls")

for record in records:
    
    print("%s is aged at %d" % (record['Name'], record['Age']))

p.free_resources()