def Sum(l,i,sum):
    s1=[]
    if i==1:
        for x in l:
            s1.append(sum+x)
        return s1
    l2=list(l)
    for x in l:
        l2.remove(x)
        s1.extend(Sum(l2,i-1,sum + x))
    return s1

def summation(l,n):
    s1=list(l)
    for i in range (2,n+1):
        s1.extend(Sum(l,i,0))
    number=1
    while True:
        if number not in s1:
            print("The least integer which is not present in the list and also cannot be represented as the summation of sub-elements is",number)
            break
        number+=1


l=[]
n=int(input("Enter the number of elements you want to add :"))
for  i in range(n):
    l.append(int(input("Enter element "+str(i+1)+":")))
summation(l,n)
