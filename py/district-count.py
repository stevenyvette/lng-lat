# coding=utf-8
#分类统计每个月的不同食品企业的区域分布

f3=open("../data/data_months/all_Maynode.csv","r")
f4=open("../data/district-coordinate.txt","r")
out=open("../data/res/name-coordinate-district-5-test.txt","w")

location={}
location_all={}
count1 = 0
error = 0
f4_len = 0
count2 = 0

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
            if abs(float(tmp[4][1:])-float(location[key][0]))<=0.00001 and abs(float(tmp[5][:-1])-float(location[key][1]))<=0.00001:
                location_all[key]=tmp[4][1:]+","+tmp[5][:-1]+","+tmp[1]+","+tmp[2]+","+tmp[3]

    except:
        error+=1

for key in location_all:
    out.write(key+","+location_all[key]+"\n")
    count2+=1

print "location:"+str(len(location))
print "location_all:"+str(len(location_all))

f3.close()
f4.close()
out.close()
