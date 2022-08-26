num=int(input("enter the number"))
fac=1
i=1
sum=0
while i<=num:
    fac=fac*i
    sum+=1/fac
    i=i+1                      
print("factor",sum)
