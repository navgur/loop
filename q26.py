i=1
k=1
while i<=5:
    s=1
    while s<=5-i:
        print(" " ,end="")
        s=s+1
    j=1
    while j<=k:
        print("*",end=" ")
        j=j+1
    k+=1
    print()
    i=i+1
i=4
while i>=1:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=4
    while j>=5-i:
        print("*",end=" ")
        j=j-1 
    # k=k+1
    print()
    i=i-1
i=5
while i>=1:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i-1 
i=5
k=1
while i>=1:
    s=4
    while s>=i-1:
        print(" ",end="")
        s=s-1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    k=k+2
    print()     
    i=i-1    
i=1
while i<=3:
    s=1
    while s<=3-1:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="") 
        j=j+1
    print()
    i=i+1  

i=1
k=1
while i<=5:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1 
    k=k+1
    print()
    i=i+1  
k=4
while k>i:
    s=1
    while s<=5-i:
        s=s+1
    j=2 
    while  j<=i:
        print(j,end=" ") 
        j=j+2
    print()
    i=i+1     
i=1
while i<=6:
     j=1
     while j<=i:
        i=1
k=1
while i<=6: 
    j=1
    while j<=i:
        if j%2==0:
            print(0,end="")
        else:    
            print(1,end="")
        j=j+1
    k=k+1
    print()
    i=i+1 
        