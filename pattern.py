for i in range(8):
    for j in range(8):
        if i==j or i+j==7:
            print("*",end="")
        else:
            print(end=" ")
    print()        