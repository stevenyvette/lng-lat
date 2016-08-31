# coding=utf-8

f=open("../data/data_months/all_Apredge.csv","r")
out=open("../data/res/type-res.txt","w")

count={}
for line in f.readlines():