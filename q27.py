i=1
k=1
while i<=3:
    s=i
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=k:
        print("*",end=" ") 
        j=j+1
    k=k+2
    print()
    i=i+1  
i=3
k=1
while i>=1:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=3
    while j>=k:
        print("*",end=" ")
        j=j-1
    k=k+2
    print()
    i=i-2    
