#Write a program that takes a number as input and checks whether it is even or odd.

# num=int(input("Enter The number:"))
# if num>0:
#  if num%2==0 :
#     print("It is an even number")
#  elif num%2==1 :
#     print("It is an odd number")
# else:
#     print("Print the valid input")

#Write a program that asks the user to enter a number and checks whether it is positive, negative, or zero.

# num1=int(input("Enter the number:"))
# if num1>0:
#    print("Positive number")
# elif num1<0:
#    print("Negative number")
# elif num1==0:
#    print("It is an zero number")

#Ask the user for their age. If age is greater than or equal to 18, print "Eligible to vote", otherwise print "Not eligible to vote".

# age=int(input("Enter the number:"))
# if age>0 and age<=100:
#     if age>=18 and age<=70:
#         print("Eligible for vote")
#     else:
#         print("Not eligible for vote")
# else:
#    print("Enter valid input")

#Take two numbers from the user and use if-else to find which one is greater.

# num2=int(input("Enter the first number:"))
# num3=int(input("Enter the secound number:"))
# if(num2>num3):
#     print("First number is an greater number")
# else:
#     print("Secound number is a greater number")

#Ask the user for their marks. If marks are greater than or equal to 40, print "Pass", else print "Fail".

# marks=int(input("Enter the marks of student:"))
# if marks>0 and marks<=100:
#     if marks>=40:
#         print("Pass")
#     else:
#         print("fail")
# else:
#       print(""Enter the valid input")

#Write a program that takes a number from the user and checks:
	# If divisible by 3 → print "Divisible by 3"
	# If divisible by 5 → print "Divisible by 5"
	# If divisible by both → print "Divisible by 3 and 5"
	# Otherwise → print "Not divisible by 3 or 5"

# num5=int(input("Enter a number:"))
# if num5%3==0 and num5%5==0:
#     print("The numbr is divisible for both of them")
# elif num5%3==0:
#     print("The numbert is Divisible by 3")
# elif num5%5==0:
#     print("The number is Divisible by 5")
# else: 
#     print("not divisible for both number")

# Take marks as input and assign grades:
# o	90 and above → A
# o	75–89 → B
# o	60–74 → C
# o	40–59 → D
# o	Below 40 → Fail

# marks1=int(input("Enter the marks:"))
# if marks1>0 and marks1<=100:
#     if marks1>=90 and marks1<=100:
#        print("Grade A")
#     elif marks1>=75 and marks1<=89:
#         print("Grade B")
#     elif marks1>=60 and marks1<=74:
#         print("Grade C")
#     elif marks1>=40 and marks1<=59:
#         print("Grade D")
#     else:
#         print("Fail")
# else:
#     print("Enter valid input")

# Ask the user to enter the balance and withdrawal amount. If withdrawal amount ≤ balance, deduct it and print remaining balance, else print "Insufficient Balance".

# balance=int(input("Enter the Balance:"))
# withdrawal=int(input("Enter the withdrawal amount:"))
# if withdrawal<=balance :
#     balance=balance-withdrawal
#     print("The remaining balance is :",balance)
# else:
#     print("Insuffient balance")

# Store a username and password. Take input from the user. If both match, print "Login Successful", else print "Invalid Credentials".
# username="Ritika"
# password=12345
# user=input("Enter the username:")
# passw=int(input("Enter the password:"))
# if(user==username and passw==password):
#     print("Login succefully")
# else:
#     print("Invalid Credentials")

# A shop gives discount based on amount:
# •	More than 5000 → 20% discount
# •	2000–5000 → 10% discount
# •	Below 2000 → No discount
# Calculate final bill.

# amount=int(input("Enter a amount:"))
# if amount>5000:
#     discount=amount*20/100
# elif amount>=2000 or amount<=5000:
#     discount=amount*10/100
# elif amount<2000:
#     print("No discount")
# final_bill=amount-discount
# print("The final bill is:",final_bill)