def duplicate(s):
    s1=""
    for x in s:
        if x not in s1:
            s1+=x
    return s1    


s=input("Enter your string:")
print("String after removing duplicates:",duplicate(s))