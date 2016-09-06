# coding=utf-8

all_location={}
month=["all_Marnode.csv","all_Aprnode.csv","all_Maynode.csv","all_Junnode.csv","all_Julnode.csv","all_Augnode.csv"]

out=open('../data/all-coordinate.txt', 'w')

for x in month:
    i="../data/data_months/"+x
    print i
    f=open(i,'r')
    for line in f.readlines():
        try:
            tmp=line.split(',')
            if not all_location.has_key(tmp[0]):
                all_location[tmp[0]]={"lng":tmp[1],"lat":tmp[2][:-1]}
        except:
            print line
    f.close()

for key in all_location:
    out.write(key+':{"lng":'+all_location[key]["lng"]+',"lat":'+all_location[key]["lat"]+'}\n')

out.close()


