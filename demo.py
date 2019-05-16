#!/usr/bin/env python
#_*_coding:utf-8_*_
#@author :yinzhengjie
#blog:http://www.cnblogs.com/yinzhengjie/tag/python%E8%87%AA%E5%8A%A8%E5%8C%96%E8%BF%90%E7%BB%B4%E4%B9%8B%E8%B7%AF/
#EMAIL:y1053419035@qq.com

end = int(input("你想要打印乘法表是:"))

row = 1
while row <= end:
    col = 1
    while col <= row:
      print(str(col) + "x" + str(row) + "=" + str(row * col) + "\t",)
    print()
    row += 1

#print("shijie,你好")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,"\t",end="")
#     print("")