i=1
k=int(65)
while i<=26:
    s=1
    while s<=26-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
    k=k+1
    print()
    i=i+1    

