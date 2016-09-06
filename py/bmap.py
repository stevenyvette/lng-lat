# coding=utf-8

f=open("../data/all-coordinate.txt",'r')
out=open("../data/bmap-coordinate-1.json",'w')

count=0
key=1
out.write("[")
for line in f.readlines():
    count+=1
    if count>2000:
        out.write("]")
        count=0
        key+=1
        file="../data/bmap-coordinate-"+str(key)+".json"
        out=open(file,'w')
        out.write("[")
    tmp=line.split(":")
    out.write(tmp[1]+":"+tmp[2]+":"+tmp[3][:-1]+',')
out.write("]")