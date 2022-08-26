# i=1
# while i<=4:
#     b=1
#     while b<=4-i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<2*i:
#         if i==4 or j==1:
#             print("*",end=" ")
#         else:
#             print(" ")
#         j=j+1
#     i=i+1
#     print()

# i=3
# while i<=6:
#     j=1
#     while j<=6-i:
#         print(" ",end="")
#         j=j+2
#     k=1
#     while k<i+1:
#         print("*",end="")
#         k=k+1
#     a=1
#     while a<6-i+1:
#         print(" ",end="")
#         a=a+1
#     b=1
#     while b<i+1:
#         print("*",end="")
#         b=b+1
#     print()
#     i=i+2
k=9
i=9
while i>=1:
    b=9
    while b>=i-2:
        print(" ",end="")
        b=b-2
    j=1
    while j<=k:
        print("*",end="")
        j=j+1
    k=k-2
    print()
    i=i-2


# i=6
# while i>=1:
#     j=6
#     while j>=i-1:
#         print(" ",end="")
#         j=j-1
#     b=6
#     while b<i*2:
#         print("*",end="")
#         b=b-1
#     print()
#     i=i-1


# card=input("insert a card")
# if card=="credit" or "debit":
#     print("card is prossing")
#     language=input("enter a language")
#     if language=="english" or "hindi" or "telugu":
#         print("enter")
#         pin=int(input("enter a pin code"))
#         if (pin>=1000):
#             print("enter")
#             type=input("enter a type of transaction")
#             if (type=="current" or "saving"):
#                 print("enter")    
#                 amount=input("enter amount")
#                 if ("100"<=amount>="100000"):
#                     print("enter")
#                     print("transaction in process")
#                     print("collect your money")
#                 else:
#                     print("not exist")
#                     recipt=input("you want recepit")
#                     if recipt=="yes":
#                         print("take a recipt")
#                         print("collect your card")
#                     else:
#                         print("take your card")
#         else:
#             print("enter worng pin")


# i=1
# while i<=4:
#     j=1
#     while j<=4-i:
#         print(" ",end="")
#         j=j+1
#     b=1
#     while b<=2*i-1:
#         if i==4 or b==1 or b==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         b=b+1
#     print()
#     i=i+1

shop=input("enter the shop name")
if shop=="shop1":
    ask=input("enter open or closed")
    if ask=="open":
        item=input("enter the item")
        if item=="biscuit":
            print("buy it")
        elif item=="kurkur":
            print("buy kukure")
        elif item=="choclate":
            print("shop is closed")
            ask2=input("open or closed")
            if ask2=="closed":
                    print("shop is closed")
        ask2=input("open or closed")
        if ask2=="closed":
            print("enter into another shop")
    
    
print("enter into another shop")
    
    
