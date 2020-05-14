n=int(input("Enter the number upto which u want your pattern:"))
for i in range(n):
    print((str(n-i)+"*")*(n-i-1)+str(n-i))
for i in range(1,n+1):
    print((str(i)+"*")*(i-1)+str(i))