n=int(input("masukan nilai n : "))
for i in range(n):
    for j in range(n):
        if(j<n-1 and j>0 and i<n-1 and i>0):
            print("#",end="")
        else:
            print("*",end="")
    print()