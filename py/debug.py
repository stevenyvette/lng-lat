# coding=utf-8

f1=open("../data/res/Apr-dis-res.txt","r")
f2=open("../data/res/Aprnode-res.txt","r")
out=open("../data/res/debug.txt","w")

a={}

for line in f1.readlines():
    tmp=line.split(",")
    a[tmp[0]]=1

for line in f2.readlines():
    tmp=line.split(",")
    if not a.has_key(tmp[0]):
        out.write(line)


