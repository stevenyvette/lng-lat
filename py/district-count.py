# coding=utf-8

f1=open("../data/data_months/all_Mayedge.csv","r")
f2=open("../data/type.txt","r")
f4=open("../data/res/location-res.txt","r")
f3=open("../data/res/Maynode-res.txt","r")
out=open("../data/res/May-dis-res.txt","w")

type={}
location={}
count={}
location_all={}
count1 = 0
error = 0
f4_len = 0
count2=0

for line in f2.readlines():
    try:
        tmp=line.split(",")
        type[tmp[0]]=tmp[1]
    except:
        continue

for line in f3.readlines():
    try:
        tmp=line.split(",")
        location[tmp[0]]=[tmp[1],tmp[2][:-1]]
    except:
        print line
        count1+=1

for line in f4.readlines():
    try:
        tmp=line.split(",")
        for key in location:
            if abs(float(tmp[4][1:])-float(location[key][0]))<=0.000001 and abs(float(tmp[5][:-1])-float(location[key][1]))<=0.000001:
                location_all[key]=tmp[4][1:]+","+tmp[5][:-1]+","+tmp[1]+","+tmp[2]+","+tmp[3]
                break
    except:
        error+=1

for key in location_all:
    out.write(key+","+location_all[key]+"\n")
    count2+=1

print "type:"+str(len(type))
print "location:"+str(len(location))
print "location_all:"+str(len(location_all))
#print len(count)
print count2
print error
#print f4_len

f1.close()
f2.close()
f3.close()
f4.close()
out.close()
