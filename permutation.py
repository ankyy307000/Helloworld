def permutation(List,String=""):
    Set=set(List)
    Stringlist=[]
    if len(Set)==1:
        String+="".join(List)
        return list([String])
    for x in Set:
        List1=list(List)
        S=String+x
        List1.remove(x)
        Stringlist.extend(permutation(List1,S))
    return Stringlist

String=input("Enter a string:")
List=permutation(list(String))
print("All the permutation of given string is :"+", ".join(List))