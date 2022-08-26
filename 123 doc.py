# i=0
# n=str(input("enter the number"))
# while i<len (n):
#     if n[i]=="1":
#         print("one")
#     elif n[i]=="2":
#         print("two")
#     elif n[i]=="3":
#         print("three")
#     elif n[i]=="4":
#         print("four")
#     elif n[i]=="5":
#         print("five")
#     else:
#         print("wrong")
#     i=i+1    
i=0
u=str(input("enter the number"))
while i<=len(u):
    if u>="1" and u<="99":
        print(u)
    i=i+1
    break            

