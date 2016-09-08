# coding=utf-8

f = open("../data/data_months/all_Maynode.csv", "r")
f2 = open("../data/res/name-coordinate-district-8-test.txt", "r")
out = open("../data/res/check.txt","w")
dic = {}
count = 0
lou = {}

for line in f.readlines():
    tmp = line.split(",")
    dic[tmp[0]] = 1

for i in range(3,9):
    f2 = open("../data/res/name-coordinate-district-"+str(i)+"-test.txt", "r")
    for line in f2.readlines():
        tmp = line.split(",")
        if dic.has_key(tmp[0]) and not lou.has_key(tmp[0]):
            out.write(line)
            lou[tmp[0]]=1
            count += 1

f.close()
f2.close()
print count