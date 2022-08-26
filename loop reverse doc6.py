i=int(input("enter the number:"))
re=0
while i>0:
    re=(re*10)+i%10
    i=i//10
print("reverse=",re)    