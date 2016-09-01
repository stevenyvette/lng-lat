# coding=utf-8

f1=open("../data/location.txt","r")
out=open("../data/res/location-res.txt","w")

for line in f1.readlines():
    tmp=line.split("!,")
    for x in tmp:
        out.write(x+"\n")