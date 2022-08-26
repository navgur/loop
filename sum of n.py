# i=int(input("enter the number"))
# fac=1
# sum=0
# while i>=0:
#     fac=fac*i
#     sum+1/fac
#     i=i+1
#     print(sum)    


i=1
list=[]
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        list.append(i)
    i=i+1
print(list)

# c=int(input("enter the number"))
# i=1
# while i<=c:
#     print("q"+str(i),"z"+str(i))
#     i=i+1
