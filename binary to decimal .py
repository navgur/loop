num=int(input("enter the number"))
sum=0
i=0
while num>0:
    rem=num%10
    sum=sum+(2**i*rem)
    num=num//10
    i=i+1
print("decimal",sum)




