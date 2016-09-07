# coding=utf-8
#将每一条区域信息分行

f1=open("../data/district-coordinate.txt","r")
out=open("../data/res/district-coordinate.txt","w")

for line in f1.readlines():
    tmp=line.split("!,")
    for x in tmp:
        out.write(x+"\n")