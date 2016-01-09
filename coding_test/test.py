# -*- coding: utf8 -*-
u'''
@summary:
@author: Administrator
@date: 
'''

if __name__ == '__main__':
    import sys
    print sys.getdefaultencoding()
    
    print u"中国"
    print unicode("中国", encoding="utf8")

#     ascii, utf8, utf16 <=> unicode <=> gbk, gb2312, gb18030
#     ascii, utf8, utf16 <=> unicode <=> gbk, gb2312, gb18030
    
    print "abc"
    
    print repr("中国"), "utf8"
    print repr(u"中国"), "unicode"
    print repr(u"abcddd")
    
    print repr("中国".decode("utf8").encode("gbk"))
    
    print repr(u"中国".encode("utf8"))
    print repr(u"中国".encode("gbk"))

    print repr(u"中国".encode("gbk").decode("gbk").encode("utf8"))

    print repr(repr)
    
# ascii 127
# 国际化翻译工作遇到问题， i18n
    
    
    