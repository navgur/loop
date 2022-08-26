num=int(input("enter any number::"))
counter=0
i=1
while i<=num:
    if num%i==0:
        counter=counter+1
    i=i+1
if counter==2:
    print("its is prime number:")
else:
    print("its not prime number::")


# # s=5
# # while s>0:
# #     j=1
# #     while j<=5:
# #         print(s,end="")
# #         j=j+1
# #     print()
# #     s=s-1
# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i-1    

