# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1

# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print('',end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*",end=" ") 
#         j=j+1
#     k=k+1
#     print()
#     i=i+1     

# i=5
# while i>0:
#     j=1
#     while j<=i:
#         j=j+5
#         print(str(i)*5)  
#     i=i-1




# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while(z<n):
#     print(z)
#     x=y
#     y=z
#     z=x+y


# i=int(input('enter the number'))
# prod=1
# while i>0:
#     prod=prod*(i%10)
#     i=i//10
#     print("product of digit",prod) 




# for row in range(6):
#     for col in range (7):
#         if (row==0 and col%3!=0)or (row==1 and col%3==0)or (row-col==2)or (row+col==8):
#             print('*',end=" ")
#         else:
#             print('',)  
# print()

i=1
while i<=5:
    s=1
    while s<5-i:
        print(" ",end="")
        s=s+1
    j=6
    while j>=i:
        print(j,end="")
        j=j-1
    print()
    i=i+1        

      
