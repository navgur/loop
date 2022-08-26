i=0
# k=65
while i<=6:
    s=1
    while s<=6-i:
        print(" ",end="")
        s=s+1 
    j=0
    k=65
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1 
i=5
while i>=0:
    s=1
    while s<=6-i:
        print(" ",end="")
        s=s+1        
    j=7
    k=65
    while j>=7-i:
        print(chr(k),end=" ")
        j=j-1
        k=k+1
    print()
    i=i-1           



