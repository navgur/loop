

# n=int(input("enter the number"))
count=0
i=1
while i<=13:
    if 13 %i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")                   
else:
    print("not prime number")    
    i=i+1    
# n=1
# while n<=100:
#     i=1
#     count=0
#     while i<=n:
#         if n%i==0:
#             count=count+1
#         i=i+1
#     if count==2:
#         print("prime number",n)
#     else:
#         print("not prime number",n)
#     n=n+1
# 
# i=1
# while i<=10:
#     a=int(input("enter the number"))
#     print(a,"whole number")
#     if a!=0 and a%2==0:
#         print(a,"even  number")
#     if a!=0 and a%2!=0:
#         print(a,"odd numbers")
#     if a!=0:
#         print(a,"natural numbers")
#     i=i+1 



name=[1,20,23,4,5,6,7,8,9,40]
i=0
while i<len(name):
    if name[i]>=20 and name[i]<=40:
        print(name[i])
    else:
        print("no number")
    i=i+1         
