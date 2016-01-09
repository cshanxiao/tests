# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2015年12月28日
'''
import csv
import json

def csv2json(datafile, separator=",", out_file="des.json"):
    u'''
    @summary: csv转换成json
    '''
    csv_obj = open(datafile, "r")
    data = csv.reader(csv_obj, delimiter=separator)

    tmp_data = []
    for row in data:
        tmp_data.append(row)
    
    json_data = json.dumps(tmp_data)
        
    file_obj = open(out_file, "w")
    file_obj.write(json_data)
    file_obj.close()
    
    with open(out_file, "w") as fd:
        fd.write(json_data)
    
    print dir(json)
    print dir(csv)
    
    print csv.__version__
    
    print "*" * 80
    for attr_str in dir(csv):
        print "attr_str", attr_str, getattr(csv, attr_str)
    print "*" * 80

if __name__ == '__main__':
    csv2json("./test.csv", ",")
    
