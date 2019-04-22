# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:09:49 2019

@author: x230
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:04:54 2019

@author: x230
"""

import pyexcel as p


def get_distance(xcord1,ycord1,xcord2,ycord2):
    distance=((xcord1-xcord2)**2 + (ycord1-ycord2)**2)**0.5
    return distance

records = p.iget_records(file_name="xys_zuobiao.xls")
#point_dict={'pname':'','xcord':'','ycord':''}
distance_list=[]


point_dict_list=[]
dis_name=''
distance_1=0.0

for record in records:
    
    
    #print("%s X_coordinate: is  %f , Y_coordinate: is  %f ," % (record['point_name'], record['xcord'], record['ycord']))
    point_dict_out={'pname':record['point_name'],'xcord':record['xcord'],'ycord':record['ycord']}
    
    #print point_dict_out
    point_dict_list.append(point_dict_out)
    """
    for record2 in records:
        point_dict_in={'pname1':record['point_name'],'xcord1':record['xcord'],'ycord1':record['ycord']}
        print point_dict_in['pname1']
        if point_dict_out['pname'] <> point_dict_in['pname1']:
            dis_name= point_dict_out['pname'] + point_dict_in['pname1']
            print dis_name
            
    """
p.free_resources()
    
dict_len=len(point_dict_list) #存入列表中点的个数

print get_distance(point_dict_list[0]['xcord'],point_dict_list[0]['ycord'],point_dict_list[1]['xcord'],point_dict_list[1]['ycord'])
#测试计算距离公式正常运作



"""    

设置一个保存结果的列表，每次计算就将结果增加到列表尾部，并记录是哪两个点之间的距离。


"""    
    



