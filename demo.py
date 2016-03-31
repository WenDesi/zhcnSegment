#encoding=utf-8

from zhcnSegment import *

if __name__ == '__main__':
    wds = Seg()
    seg_list = wds.cut("他来到了网易杭研大厦",False)
    print(", ".join(seg_list))