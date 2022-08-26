 
 
# n=int(input("enter the number"))
i=1
while i<=5:
    s=1
    while s<=5-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(i-j+1,end="")
        j=j+1
    j=1
    while j<i:
        print(j+1,end="")
        j=j+1
    print()
    i=i+1  
          
