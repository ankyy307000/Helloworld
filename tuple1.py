
t=(1,2,1,3,4,5,6,5,4,2,3)
i=0
for x in t:
    if t.index(x)==i:
        print("No of occurence of ",x," : ",t.count(x))
    i+=1
