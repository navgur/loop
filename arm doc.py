# a=int(input("enter the number"))
i=int(input("enter the  number"))
orig=i
length=len(str(i))
sum=0
while i>=0:
    # sum=sum+(i%10)*(i%10)*(i%10) 
    sum+=(i%10)**length
    i=i//10
if orig==sum:
    print("arm")
else:
    print("wrong number")        