# i=1
# while i<=10:
#     print(i,end=",")
#     if i==8:
#      break
#     i=i+1
# i=1
# while i<=10:
#     print(i,end=",")
#     if i==9:
#         break
#     i=i+1


# num=int(input("enter the number "))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1
# if num==sum:
#     print(num,"is perfect number")
# else:
#     print(num,"is not perfect number") 
# 
#    


a=int(input("enter the number"))
num=int(input("enter number of digit"))
x=a
i=1
sum=0
while i<=a:
    rev=a%10
    a//=10
    sum+=rev**num
print(sum)
if (sum==x):
    print("armstrong number")
else:
    print("not arm")    
i=i+1
