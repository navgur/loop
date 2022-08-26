# num=int(input("enter the number"))
# i=1
# while i<=num:
#     if num%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")
n=int(input("enter the number"))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not prime")
    i=i+1 
  
# i=1    
# count=0       
# while i<=5:
#     if 5%i==0:
#          count=count+i
#     i=i+1
# if count==2:
#     print("prime number") 
# else:
#     print("not prime")

        
