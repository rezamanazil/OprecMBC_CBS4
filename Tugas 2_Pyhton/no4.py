x=int(input("masukan nilai n : "))
for i in range(x):
    for j in range(x):
        if(j<x-1 and j>0 and i<x-1 and i>0):
            print("#",end="")
        else:
            print("*",end="")
    print()
