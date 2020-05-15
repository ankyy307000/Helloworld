a=[]
n=int(input("Enter the number of element you want in your list:"))
for x in range(n):
    a.append(input("Enter element "+str(x+1)+":"))

unique=[]
for x in a:
    if x not in unique:
        unique.append(x)

print("Non duplicate items:")
print(unique)