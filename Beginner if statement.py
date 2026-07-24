# 1. Office Entry System
# Story:
# A company allows employees to enter only if they have a valid ID card.
# Question:
# Write a program that asks whether the employee has an ID card (yes/no).
# If yes, print:
# "Access Granted"
# Otherwise, do nothing.

# Solution:-
# print("Office Entry System")
# emp=int(input("Enter an ID:"))
# emp1=int(input("Enter confirm id:"))
# if emp==emp1:
#     print("Acess Granted")
# # __________________________________________________________________

# 2. Movie Ticket
# A movie is only for people aged 18 or above.
# Take age as input.
# If eligible, print:
# You can watch the movie.

# Solution:-
# print("Movie Ticket")
# age=int(input("Enter the age:"))
# if age>=18:
#     print("You can able to watch movie")

# ________________________________________

# 3. Online Shopping
# Amazon gives free delivery only if the order amount is above ₹999.
# Take order amount.
# If eligible, print:
# Free Delivery Applied

# Solution:-
# print(" Online Shopping")
# amount=int(input("Enter the amount:"))
# if amount>999:
#     print("Free Delivery")

# ________________________________________

# 4. College Attendance
# A student can write the exam only if attendance is 75% or above.
# Take attendance percentage.
# Print:
# Eligible for Exam

# Solution:-
# print("College Attendance")
# attendance=int(input("Enter total number of attendance:"))
# if attendance > 75:
#     print("You are eligible to write the exam beacuse your attendance above 75%")
# # ________________________________________

# 5. Gym Membership
# Only members can enter the gym.
# Ask:
# Are you a member?
# If yes, allow entry.

# Solution:-
# print("Gym Membership")
# entry=input("Are you a member:")
# if entry=='yes':
#     print("Allow entry")
# ________________________________________

# if- else

# 6. Bank ATM
# Story
# A customer wants to withdraw money.
# Ask:
# •	Account Balance 
# •	Withdrawal Amount 
# If balance is sufficient
# Transaction Successful
# Else
# Insufficient Balance

# Solution:-
# print("Bank ATM")
# account_balance=int(input("Enter the account balance:"))
# withdrawal_amount=int(input("Enter the withdrawal amount:"))
# if withdrawal_amount<=account_balance:
#     print("Transaction Successful")
# else:
#     print("Insufficient Balance")

# ________________________________________

# 7. Password Verification
# Take password from the user.
# Correct password:
# Python@123
# If correct
# Login Successful
# Else
# Invalid Password

# Solution:-
# print(" Password Verification")
# password=input("Enter the password:")
# password1=input("Enter confirm password:")
# if password==password1:
#     print("Login Successful")
# else:
#     print("Invalid Password")
# ________________________________________

# 8. Restaurant Bill
# If bill amount is more than ₹500
# Apply 10% discount
# Otherwise
# No discount.

# Solution:-
# print("Restaurant Bill")
# bill=int(input("Enter the bill amount:"))
# if bill>500:
#     amount=bill*0.90
#     print(amount)
# else:
#     print("No Discount")
# # ________________________________________

# 9. Cricket Stadium
# Only people having tickets can enter.
# Input:
# Do you have ticket?
# Display appropriate message.

# Solution:-
# print("Cricket Stadium")
# ticket=input("Do you have tickets:")
# if ticket=='yes':
#     print("You can enter in stadium")
# else:
#     print("Not allowed")
# ________________________________________

# 10. Petrol Pump
# A customer wants petrol worth ₹2000.
# If wallet balance is enough
# Fill petrol
# Else
# Transaction Failed

# Solution:-
# print("Petrol Pump")
# balance=int(input("Enter the wallet balance:"))
# amount=int(input("Enter the pertrol worth:"))
# if balance<amount:
#     print("Tansaction Failed")
# else:
#     print("Fill Petrol")
# ________________________________________

# Level 3: if-elif-else

# 11. Student Grade System
# Marks:
# 90+
# Grade A
# 80+
# Grade B
# 70+
# Grade C
# Else
# Fail

# # Solution:-
# print("Student Grade System")
# marks=int(input("Enter the marks:"))
# if marks>0 and marks<100:
#     print("Print Valid marks")
# if marks>90 and marks<=100:
#     print("Grade A+")
# elif marks>=80 and marks<90:
#     print("Grade B+")
# elif marks>=70 and marks<80:
#     print("Grade C+")
# else:
#     print("Fail")

# ________________________________________

# 12. Electricity Bill
# Monthly Units
# 0-100
# No charge
# 101-300
# ₹5/unit
# 301-500
# ₹8/unit
# Above 500
# ₹10/unit

# Solution:-

# print("Electricity Bill")
# bill=int(input("Enter the bill:"))
# if bill

# ________________________________________

# 13. Employee Bonus
# Experience
# Less than 2 years
# No Bonus
# 2-5 years
# ₹10,000
# 5-10 years
# ₹25,000
# More than 10
# ₹50,000

# Solution:-
# print("Employee Bonus")
# experience=int(input("Enter the experience:"))
# if experience<=2:
#     print("No Bonus")
# elif experience<=5:
#     print("Bonus will be 10,000")
# elif experience<=10:
#     print("salary will be 25,000")
# else:
#     print("Salary will be 50,000")
# if experience<0:
#     print("Print the valid experience")
# ________________________________________

# 14. Income Tax
# Income
# Less than ₹5L
# No Tax
# ₹5L-10L
# 10%
# ₹10L-20L
# 20%
# Above ₹20L
# 30%

# Solution:-
# tax=0
# print("Income Tax")
# income=int(input("Enter the income:"))
# if income<500000:
#     print("No Tax")
# elif income<=1000000:
#     tax=income*10/100
#     print("Tax will be :",tax)
# elif income<=200000:
#     tax=income*20/100 
#     print("Tax will be:",tax)
# else:
#     tax=income*30/100
#     print("Tax will be:",tax)

#  ________________________________________

# 15. Mobile Recharge
# Recharge Amount
# ₹99
# Basic Pack
# ₹199
# Standard
# ₹399
# Premium
# Otherwise
# Invalid Recharge

# Solution:-
# print("Mobile Recharge")
# recharge_amount=int(input("Enter the recharge amount:"))
# if recharge_amount==99:
#     print("Basic Pack")
# elif recharge_amount==199:
#     print("Standard")
# elif recharge_amount==399:
#     print("Premium")
# else:
#     print("Inavalid Recahrge")
# ________________________________________

# Level 4: Nested if

# 16. Company Interview
# Candidate must satisfy
# Age >=21
# AND
# Degree = BE/BTech
# Then eligible.
# Else not eligible.

# Solution:-
# print("Company Interview")
# age=int(input("Enter the age:"))
# degree=input("Enter the degree:")
# if age>=21:
#     if degree=='BE/Btech':
#         print("Then eligible")
#     else:
#         print("Not eligible")

# ________________________________________

# Bank Loan
# Conditions
# Salary > ₹40,000
# AND
# Credit Score >700
# Loan Approved
# Else
# Rejected

# Solution:-
# print("Bank Loan")
# salary=int(input("Enter the salary:"))
# credit=int(input("Enter the credit:"))
# if salary>40000:
#     if credit>700:
#         print("Loan Approved")
#     else:
#         print("Rejected")

# ________________________________________
# 18. School Admission
# Student should
# Age >=5
# If yes
# Check documents
# If documents available
# Admission Confirmed
# Else
# Bring Documents

# Solution:-

# print("Student Admission")
# age=int(input("Enter the age:"))
# if age>=5:
#         age1=input("Enter the documents available or not:")
#         if age1=="documents available":
#                print("Admission Confirmed")
#         else:
#               print("Bring Documents")
# # ________________________________________

# 19. Flight Boarding
# Passenger has ticket?
# If yes
# Passport verified?
# If yes
# Board Flight
# Else
# Verification Failed

# Solution:-
# print("Flight Boarding")
# ticket=input("Passenger has ticket:")
# if ticket=="yes":
#     print("Passport Verified")
# passenger=input("Passport verfied or not:")
# if passenger=="yes":
#     print("Board Flight")
# else:
#     print("Verification Failed")
# # ________________________________________

# 20. Online Exam
# Student Login
# If username correct
# Check password
# If password correct
# Start Exam
# Else
# Wrong Password

# Solution:-
# username=input("Enter the username:")
# confirm_username=input("Enter the confirm username:")
# if username==confirm_username:
#     print("Check Password")
#     password=int(input("Enter the password:"))
#     confirm_password=int(input("Enter the confirm password:"))
#     if password==confirm_password:
#         print("Start Exam")
#     else:
#         print("Wrong Password or username")
# # ________________________________________

# Level 5: Real-Time Business Scenarios
# 21. Food Delivery
# If restaurant is open
# Check delivery partner availability
# If available
# Order Accepted
# Else
# No Delivery Partner
# Else
# Restaurant Closed

# Solution:-
# print("Food Delivery")
# restaurant=input("Is restaurant open or not:")
# if restaurant=="open":
#      print("Yes it is open")
# else:
#      print("Not open")
# delivery=input("Check delivery partner avilable or not:")
# if delivery=="yes":
#      print("Order Accepted")
# else:
#      print("No delivey partner")
#      print("Restaurant Closed")
# # ________________________________________

# 22. Hospital Appointment
# Doctor Available?
# If yes
# Patient registered?
# If yes
# Appointment Confirmed
# Else
# Register First

# Solution:-
# print("Hospital Appointment")
# doctor=input("Is Doctor Available:")
# if doctor=="yes":
#     print("Yes Available")
# if doctor=="no":
#     print("No not avaiable")
# patient=input("Is patient registed:")
# if patient=="yes":
#     print("Patient Registed")
# if patient=="no":
#     print("Not have registed")
# appointement=input("Is appointment confirmed:")
# if appointement=="yes":
#     print("Ok you may visit to doctor")
# if appointement=="no":
#     print("Register First")

# ________________________________________

# 23. Railway Reservation
# Seats Available?
# If yes
# Book Ticket
# Else
# Waiting List

# Solution:-

# print("Railway Reservation")
# seates=input("Is setaes available:")
# if seates=="yes":
#     print("Book Tickets")
# else:
#     print("Waiting List")
# ________________________________________

# 24. Hotel Booking
# Room Available?
# If yes
# Advance Payment Done?
# If yes
# Booking Confirmed
# Else
# Pay Advance

# Solution:-
# print("Hotel Booking")
# room=input("Is Room Available:")
# if room=="yes":
#     print("Check if Advance Payment done or not:")
# payment=input("Is payment advance done? ")
# if payment=="yes":
#     print("Booking Confirmed")
# else:
#     print("Pay Advance")


# ________________________________________

# 25. Laptop Purchase
# Budget
# Below ₹40,000
# Basic Laptop
# ₹40,000-70,000
# Mid-range
# Above ₹70,000
# Gaming Laptop

# Solution:-
# budget=int(input("Enter the budget:"))
# if budget<40000:
#     print("Basic Laptop")
# if budget>40000 and budget<70000:
#     print("Mid Range")
# if budget>70000:
#     print("Gaming Laptop")

# ________________________________________

# Level 6: MNC Interview Logical Scenarios
# 26. Salary Hike
# Employee Rating
# 5
# 30% hike
# 4
# 20%
# 3
# 10%
# Below 3
# No hike

# Solution:-
# employee=int(input("Enter the rate:"))
# if employee==5:
#     print(f"30% hike")
# if employee==4:
#     print(f"20% hike")
# if employee==3:
#     print(f"10% hike")
# if employee<3:
#     print("No hike")
# else:
#     print("Invalid hike")
# # ________________________________________

# 27. Software License
# If license active
# Check expiry date
# If expired
# Renew License
# Else
# Software Opens

# Solution:-
# license=input("Enter if license active:")
# if license=="yes":
#     print("Check expired")
# license1=input("Enter if license expired:")
# if license1=="no":
#     print("Renew License")
# else:
#     print("Software Opens")
# # ________________________________________

# 28. E-commerce Coupon
# Order Amount > ₹5000
# AND
# Coupon Available
# Apply 20%
# Otherwise
# No Discount

# Solution:-

# amount=int(input("Enter the order amount:"))
# if amount>5000:
#     discount=input("Enter the discount available:")
#     if discount=="available":
#         print("Apply 20% ")
#     else:
#         print("No Discount")
# ________________________________________

# 29. Hospital Emergency
# Patient Condition
# Critical
# Immediate ICU
# Serious
# Emergency Ward
# Normal
# General Ward

# Solution:-
# patient=input("Patient condition:")
# if patient=="critical":
#     print("Immediate ICU")
# if patient=="Serious":
#     print("Emergenct Ward")
# if patient=="Normal":
#     print("General Ward")

# ________________________________________

# 30. Airport Security (Story-Based)
# Story
# Rahul reaches the airport for an international flight.
# Security follows these rules:
# •	Passenger must have a valid ticket. 
# •	Passport must be valid. 
# •	Visa must be valid. 
# •	Baggage weight must not exceed 30 kg. 
# If all conditions are satisfied:
# Boarding Allowed
# Otherwise, print the appropriate reason, such as:
# •	Ticket Missing 
# •	Passport Invalid 
# •	Visa Invalid 
# •	Excess Baggage 

# Solution:-

# passenger=input("Is passenger has valid ticket:")
# if passenger=="no":
#         print("Ticket Missing")
# if passenger=="yes":
#     passport=input("Is having the valid passport:")
#     if passport=="no":
#          print("Passport Invalid")
#          if passport=="yes":
#              visa=input("Is having the valid visa:")
#              if visa=="no":
#                  print("Visa Invalid")
#                  if visa=="yes":
#                       weight=input("Is baggage weight is not exceed 30kg:")
#                       if weight=="no":
#                            print("Excess Baggage")
#                            if weight=="yes":
#                                 print("Bording Allowed")
        
    
    

# ________________________________________

# Bonus Challenge (Real MNC Scenario)
# Online Banking Login
# Story
# A customer wants to transfer ₹50,000.
# The bank checks the following conditions:
# 1.	Username should be correct. 
# 2.	Password should be correct. 
# 3.	OTP should be correct. 
# 4.	Account balance should be greater than transfer amount. 
# 5.	Daily transfer limit should not exceed ₹1,00,000. 
# If every condition is satisfied:
# Transaction Successful
# Otherwise, display the first appropriate error message.

# tranfer_amount=50000
# username=input("Enter the username:")
# confirm_username=input("Enter confirm username:")
# if username==confirm_username:
#         print("Its an vaid username")
#         if username!=confirm_username:
#              print("Print Valid username")
#         else:
#             password=input("Enter the password:")
#             confirm_password=input("Enter the confirm password:")
#             if password!=confirm_password:
#                 print("Invalid Password")
#             else:
#                 otp=int(input("Enter otp:"))
#                 confirm_otp=int(input("Enter the confirm otp:"))
#                 if otp!=confirm_otp:
#                     print("Invalid Otp")
#                 else:
#                     amount=int(input("Enter the account balance:"))
#                     if amount>tranfer_amount:
#                         print("Insuffient balance")
#                         if tranfer_amount<=100000:
#                             print("Daily transfer limit exceeded")
#                         else:
#                              print("Transaction Sucessfully")
            