def perfect(num):
 i=1 
 while i<=num:
    sum=0
    j=1
    while j<i:
     if i%j==0:
        sum=sum+j
     j=j+1
    if sum==i:
        print("perfect number")
    else:
        print("not perfect numbers")
    i=i+1
x=int(input("enter  the number"))
perfect(x)

    
# card=input("insert a card")
# if card=="credit" or "debit":
#     print("card is prossing:--")
#     language=input("enter a language:--")
#     if language=="english" or "hindi" or "telugu":
#         print("click")
#         pin=str(input("enter a pin code:--"))
#         if len(pin)==4:
#             print("click")
#             type=input("enter a type of transaction:---")
#             if (type=="current" or "saving"):
#                 print("click")    
#                 amount=int(input("enter amount:---"))
#                 if (100>=amount or amount<=100000):
#                     print("click")
#                     print("transaction in process")
#                     print("collect your money")
#                     recipt=input("do you want recipt")
#                     if  recipt=="yes":
#                         print("take a recipt")
#                         print("collect your card and take money")
#                     else:
#                         print("ok take your money and card")
#                 else:
#                     print("not exist")
#                     print("below 500 we can't give the money")
#                     recipt=input("you want recepit:--")
#             else:
#                  print("withdraw")     
#         else:
#             print("enter wrong pin")
              

