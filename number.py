a=int(input("Enter your number:"))
if a%2==0 :
    print("Your number is even")
else:
    print("Your number is odd")

for i in range(2,a):
    if(a%i==0):
        print("Your number is Not Prime")
        break
else:
    print("Your number is Prime")

rev=0
x=a
while a>0:
    d=a%10
    a=a//10
    rev=rev*10+d  
if x==rev :
    print("Your number is pallindrome")
else:
    print("Your number is not pallindrome")

arm=0
y=x
while x>0:
    d=x%10
    x=x//10
    arm=arm+(d**3) 
if y==arm:
    print("Your number is armstrong")
else:
    print("Your number is not armstrong")