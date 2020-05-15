l1=[]
len1=int(input("Enter lenth of list 1:"))
for x in range(len1):
    l1.append(input("Enter element " + str(x+1) + ":"))
l2=[]
len2=int(input("Enter lenth of list 2:"))
for x in range(len2):
    l2.append(input("Enter element " + str(x+1) + ":"))

l=list(set(l1)&set(l2))
print("intersection of lists 1 and 2:")
for x in range(len(l)):
    print(l[x],end=" ")
