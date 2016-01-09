# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 2016年1月6日
'''

class QQ_parser(object):
    
    def get_qq(self, file_name, save_path):
        '''
        @summary: 获取QQ号码
        '''
    #     1 打开文件
    #     2 读取内容，分析得到qq号
    #     3 保存qq号码
        
        qq_set = set()

#         src_file = open(file_name, "r")
#         lines = src_file.readlines()
#         
#         for line in lines:
#             line = line.strip()
#             if not ("(" in line and ")" in line):
#                 continue                
#             qq_set.add(line.split("(")[1].split(")")[0])
#         src_file.close()
#             
#         des_file = open(save_path, "w")
#          
#         for qq in qq_set:
#             des_file.write(qq + "\n")
#  
#         des_file.writelines("\n".join(qq_set))
#         des_file.close()


        try:
            with open(file_name, "r") as src_file:
                lines = src_file.readlines()
                for line in lines:
                    line = line.strip()
                    if not ("(" in line and ")" in line):
                        continue                
                    qq_set.add(line.split("(")[1].split(")")[0])
        except IOError:
            print "file not found!file_name(%s)" % file_name
        
        try:
            with open(save_path, "w") as fd:
                fd.writelines("\n".join(qq_set))
        except IOError:
            print "file not found!save_path(%s)" % save_path
        
        
if __name__ == '__main__':
    parser = QQ_parser()
    parser.get_qq("./qq_jl.txt", "./qq.txt")
    print "parser finshed!"



