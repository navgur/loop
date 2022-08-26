# i=1
# while i<=10:  
#  print(i,i**2)
#  i=i+1

# i=10
# while i<=300:
#     print(i)
#     i=i+10

# i=105
# while i>=7:
#     print(i)
#     i=i-1
    # print(i)
    # i=i-7

# i=1
# while i<=10:
#     a=int(input("enter the number"))
#     print(a,"whole number")
#     if a!=0 and a%2==0:
#         print(a,"even number")
#     if a!=0 and a%2!=0:
#         print(a,"odd number")
#     if a!=0:
#         print(a,"natural number")
#     i=i+1            

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i=i+2    

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     print(sum)
#     i=i+1

# i=1
# sum=0
# while i<=10:
#    if i%2==0:
#     sum=sum+i
#     print(sum)
#    i=i+1
# n=int(input("enter the number"))
# i=1
# while i<=10:
#     table=n*i
#     print(table)
#     i=i+1    


# i=int(input("enter the number"))
# n=int(input("enter the number"))
# # i=int(input("enter the number"))
# while i<=n:
#     if i%2==0:
#      print(i)
#     i=i+1

# i=1
# count=0
# while i<=13:
#     if 13%i==0:
#         count=count+1
#     i=i+1      
# if count==2:
#         print("prime number")
# else:
#         print("not prime") 
#         # i=i+1    


# i=int(input("enter the number"))
# pro=1
# while i>0:
#     pro=pro*(i%10)
#     i=i//10
# print("digit of product",pro)

# i=245
# sum=0
# while i>0:
#     sum=sum+i%10
#     i//=10
# print("sum of digit=",sum)


# # i=int(input("enter the number"))
# # rev=0
# # while i>0:
# #     rev=(rev*10)+i%10
#     i=i//10
# print("rever=",rev)    
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
#     elif n[i]=="6":
#         print("six")
#     i=i+1
# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# i=int(input("enter the number"))
# org=i
# l=len(str(i))
# sum=0
# while i>0:
#     sum+=(i%10)**l
#     i=i//10
# if org==sum:
#     print("armstrong")
# else:
#     print("not armstrong")

# i=int(input("enter the number"))
# fac=1
# while i>0:
#     fac=fac*i
#     i=i-1
# print("factorial of digit=",fac)   


# num=int(input("enter the number"))
# sum=0
# i=0
# while num>0:
#     rem=num%10
#     sum=sum+(2**i*rem)
#     num=num//10
#     i=i+1
# print("decimal",sum)

# num=int(input("enter the binary number:"))
# sum=0
# i=0
# while num>0:
#     rem=num%10
#     sum=sum+(2**i*rem)
#     num=num//10
#     i=i+1
# print("decimal",sum)
# num=int(input("enter the number"))

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1    

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(6-j,end="")
#         j=j+1
#     print()
    # i=i-1

# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i-1    


# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i-1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1    


# i=5
# while i>=1:
#     j=5
#     while j>=i:
#         print(j,end="")
#         j=j-1
#     print()
#     i=i-1  

# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="") 
#         s=s+1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1   

# i=5
# while i>=1:
#     j=6
#     while j>i:
#         print(j-i,end="")
#         j-=1
#     print()
#     i=i-1

# i=5
# while i>=1:
#     #  s=1
#     #  while s<=i-1:
#     #     print(" ",end="")
#     #     s=s+1
#      j=6    
#      while j>i:
#         print(j-i,end="")
#         j=j-1
#      print()
#      i=i-1
# k=1
# i=1
# while i<=4:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print(k,end="")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1  
# 
# i=1
# k=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(k,end="")
#         j=j+1
#         k=k+1
#     print()
    # i=i+2  

# i=0
# while i<=4:
#     j=0
#     while j<=i:
#         print(j*i,end="") 
#         j=j+1
#     print()
#     i=i+1     

# i=0
# while i<=5:
#     j=0
#     while j<=i:
#         print(j**2,end="")
#         j=j+1
#     print()
#     i=i+1    

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i**2,end="")
#         j=j+1
#     print()
#     i=i+1    

# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(i,end="")
#         j=j+2
#     print()
#     i=i+2    
       

#*** print

# i=1
# k=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     k=k+1    
#     print()
#     i=i+1  
        
# i=4
# k=1
# while i>=1:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=4
#     while j>=5-i:
#         print("*",end=" ")
#         j=j-1
#     k=k+1
#     print()
#     i=i-1            
    
    
    
    
    
    
    
# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1 
# i=4
# while i>=1:
#     s=1
#     while s<=5-i:
#         print(" ",end="") 
#         s=s+1
#     j=4
#     while j>=5-i:
#         print("*",end=" ")
#         j=j-1
#     print()
#     i=i-1    

           #  "binary number"
           
# i=0
# while i<=10:
#     j=0
#     while j<=i:
#         print(j%2,end="")
#         j=j+1
#     print()
#     i=i+1    
          

# i=5
# while i>=1:
#     j=6
#     while j>i:
#         print(j-i,end="")
#         j=j-1
#     print()
#     i=i-1     



# i=5
# while i>=1:
#     #  s=1
#     #  while s<=i-1:
#     #     print(" ",end="")
#     #     s=s+1
#      j=6    
#      while j>i:
#         print(j-i,end="")
#         j=j-1
#      print()
#      i=i-1

# i=0
# while i<=4:
#     j=0
#     while j<=i:
#         print(i+j%2,end="")
#         j=j+1
#     print()
#     i=i+1    
                

# # n=int(input("enter the number"))
# # i=0
# # while i<=n:
# #     j=0
# #     while j<=i:
# #         print(j,end="")
# #         j=j+1
# #     print()
# #     i=i+1
# # i=0
# # while i<=10:
# #     i=i+1
# #     if i==3:
# #         continue
# #     if i==6:
# #         continue
# #     print(i)

# i=5
# while i>=1:
#     j=6
#     while j>=i:
#         if j%2!=0:
#             print(j-1,end="")
#             j=j+1
#     print()
#     i=i+1            
    
# i=0
# while i<=10:
#     a=i
#     while a!=0:
#         print(a%2, end="")
#         a=a//2
#     print()
#     i+=1
# while i<=10:
#     a=i
#     while a!=0:
#         print(a%2,end="")
#         a=a//2
#     print()
    # i=i+1    


# i
# a=str(input("enter the character"))
# i=0
# l=len(a)
# while i<l:
#    j=0
#    while j<=i:
#         print(a[j],end="") 
#         j=j+1
#    print()
#    i=i+1

# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+2  
# i=4
# while i>=1:
#     s=1
#     while s<=6-i:
#         print(" ",end="")
#         s=s+1
#     j=4
#     while j>=6-i:
#         print("*",end= " ")
#         j=j-1
#     print()
#     i=i-2    

    
    

# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1        
# i=5
# while i>=1:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print(j,end=" ") 
#         j=j+1
#     print()
#     i=i-1           

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(j,end="")
#         j=j+1
#     print()
#     i=i+1    

#"python print"


# a=str(input("enter the character"))
# l=len(a)
# i=0
# while i<l:
#     # s=1
#     # while s<=5-i:
#     #     print(" ",end="")
#     #     s=s+1
#     j=0
#     while j<=i:
#         print(a[j],end="")
#         j=j+1
#     print()
#     i=i+1    

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(i,end="")
#         j=j+1
#     print()
#     i=i+1    


# i=1
# while i<=5:
#     j=1
#     k=65
#     while j<=i:
#         print(chr(k),end="")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1    

# i=1
# k=65
# while i<=5:
#     j=1
#     while j<=i:
#         print(chr(k),end="")
#         j=j+1
#         k=k+1
#     print()
#     i=i+1 
# 
# i=1
# while i<=8:
#     s=1
#     while s<=8-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+2      
# i=1
# while i<=8:
#     s=1
#     while s<=8-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+2  
# i=1
# while i<=5:
#     s=1
#     while s<=5-i:
#         print(" ",end="")
#         s=s+1
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+2 

# i=4
# while i>=1:
#     s=1
#     while s<=6-i:
#         print(" ",end="")
#         s=s+1
#     j=4
#     while j>=6-i:
#         print("*",end=" ")
#         j=j-1
#     print()
#     i=i-2        
# for i in range(10,1,-1):
#      print(i)

n=int(input("enter the number"))
a=int(input("enter the number"))
while n<=a:
    i=1
    while i<=10:
        print(n*i)
        i=i+1
    print()    
    n=n+1        





