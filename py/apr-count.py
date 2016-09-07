# coding=utf-8

f1=open("../data/data_months/all_Augedge.csv","r")
f2=open("../data/name-type.txt","r")
out=open("../data/res/type-count-Aug.txt","w")

dic={}
count={}

for line in f2.readlines():
    try:
        tmp=line.split(",")
        dic[tmp[0]]=tmp[1][:-1]
    except:
        print line

print "second"

for line in f1.readlines():
    try:
        tmp=line.split(",")
        if count.has_key(dic[tmp[0]]):
            count[dic[tmp[0]]]+=1
        else:
            count[dic[tmp[0]]]=1
    except:
        print line
print "third"

for key in count:
    out.write(key+":"+str(count[key])+"\n")

f1.close()
f2.close()
out.close()

