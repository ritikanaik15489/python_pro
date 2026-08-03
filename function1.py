# def Addition():
#     num1=10
#     num2=20
#     add=num1+num2
#     print(add)
# Addition()

# def Addition(num1,num2):
#     add=num1+num2
#     print(add)
# Addition(70,10)

# num1=20
# num2=10
# add=num1+num2
# print(add)

# def EvenNo():
#     for i in range(1,10+1):
#         if i%2==0:
#             print(i)
# EvenNo()

# Global variable
# num3=10
# def Multiplication():
#     num2=3
#     # manipulation is done
#     global num3
#     num3=50
#     mul=num3*num2
#     print(mul)
# Multiplication()

# def Addition():
#     num4=20
#     add=num3+num4
#     print(add)
# Addition() 
# it will give the new output as 50+20=70 not 10+20=30 because of gloabl variable is declares or manipulation
# if we cooment to gloabl avariable and new declare variable then the output wil give as 10+2=30

# Types of parameters

# positional parameter / arugements

# def Addition(num1,num2):
#     add = num1+num2
#     print(add)
# Addition(10,30)
# Addition(50,70)
# Addition() is an arugemensts it is reusable bloack of code
# num1=10
# num2=20
# Accsesing by postion 

# keyord 

# def Addition(num1,num2):
#     add=num1+num2
#     print(add)
#     print(num1,num2)
# Addition(num1=10,num2=20) keyword parameter

# Default

# def Addition(num1,num2=30):
#     add=num1+num2
#     print(add)
# Addition(10,20)
# Addition(40)
# the deafult parameter is passed in def function so the num2=30 will consider has 2 and 
# num1 value has been passsed in arguments

# Why we use variable length

# def Addition(*add):
#     print(add)
# Addition(10,20,30,40,50)

# * is used for single value whivh will helps to print the o/p in positional way

# def std_info(**age):
#     print(age)
# std_info(Roshan=25,roshani=23)

# ** is usd to accept the key and value pair 

# def Addition(num1,num2,/):
#     add=num1+num2
#     print(add)
# Addition(10,20)
# Addition(num1=10,num2=40)
# TypeError: Addition() got some positional-only arguments passed as keyword arguments: 'num1, num2'
# works as positional arugments accept the positional arugement instead of keywords


# def Addition(*,num1,num2):
#     add=num1+num2
#     print(add)
# Addition(num1=10,num2=40)
# Addition(10,20)
# TypeError: Addition() takes 0 positional arguments but 2 were given
# works as an keyword arugements and accept only keyword arugements


# def Bank_Customer_Detail(bname="TKA",bifsc="Tksff",baad="Chichwad",/,*,cname,bal):
#     print(f"""
#                  Bank name:{bname}
#                  Bank IFSC Code:{bifsc}
#                  Bank Address:{baad}
#                  Customer name:{cname}
#                  Balance:{bal}



#     """)
# Bank_Customer_Detail(cname="Roshani",bal=8000)
# # Can upadate the data
# Bank_Customer_Detail("SBI","SBI123","Pune",cname="Ritika",bal=10000)

# Bank_Customer_Detail(bname="SBI",bifsc="SBI123",baad="Pune",cname="Ritika",bal=10000)
# +TypeError: Bank_Customer_Detail() got some positional-only arguments passed as keyword arguments: 'bname, bifsc, baad'

# def Addition(num1=10,num2):
#     add=num1+num2
#     print(add)
# Addition(10,20)
# deafult parameter has to be passed at the right side only not on the left side 

# def Mul(num1,num2):
#     mul=num1*num2
#     print(mul)
# Mul(num1=20,30)
# SyntaxError: positional argument follows keyword argument
# deafult value are passed at left not on the right in arguments

# def Addition(num1,num2):
#     add=num1+num2
#     print(add)
# def Mul(num1,num2):
#     Addition(10,90)
#     mul=num1*num2
#     print(mul)
# Mul(10,20)

# def Addition(num1,num2):
#     add=num1+num2
#     print(add)
# def Mul():
#     Addition(10,90)
#     mul=num1*num2
#     print(mul)
# Mul()


