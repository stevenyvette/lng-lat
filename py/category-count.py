# coding=utf-8

f=open("../data/type.txt","r")
out=open("../data/res/type-res.txt","w")

count={}
for line in f.readlines():
    try:
        tmp = line.split(",")
        if count.has_key(tmp[1]):
            count[tmp[1]]+=1
        else:
            count[tmp[1]]=1
            print tmp[1]
    except:
        continue

for key in count:
    out.write(key[:-1]+":"+str(count[key])+"\n")

f.close()
out.close()