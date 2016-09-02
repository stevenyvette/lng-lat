# coding=utf-8

f = open("../data/res/Maynode-res.txt", "r")
f2 = open("../data/res/Jul-dis-res.txt", "r")

dic = {}
count = 0

for line in f.readlines():
    tmp = line.split(",")
    dic[tmp[0]] = 1

for line in f2.readlines():
    tmp = line.split(",")
    if dic.has_key(tmp[0]):
        count += 1

f.close()
f2.close()
print count