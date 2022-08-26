i=int(input("enter the number"))
num=int(input("enter the number"))
sum=0
sum2=0
while i<=num:
    if i%2==0:
        sum=sum+i
    if i%2!=0:
        sum2=sum2+i
    i=i+1
print("even",sum)
print("odd",sum2)    



