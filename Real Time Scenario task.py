print("TASK 1")

print("Employee Salary Management System")
name="Management System"
Emp_id=101
Employee_name="Ritika"
Employee_salary=50000
Employee_department="Python"
print(f"""
        {name}
           Employee Details
      Employee Id:{Emp_id}
      Employee Name:{Employee_name}
      Employeee Salary:{Employee_salary}
      Employee Department:{Employee_department}
      """)

print("--------------------------------------------------------------------------------------------")

print("TASK 2")

print("E-Commerce Product Information")
name="Flipkart"
Product_id=201
Product_name="Washing Machine"
Product_price=20000
Product_stock=1000
Ordered_quantity=20
Remaining_stocks=(Product_stock)-(Ordered_quantity)
print(f"""
            {name}
           Product Details
      Product Id:{Product_id}
      Product Name:{Product_name}
      Product Price:{Product_price}
      Product Stock:{Product_stock}
      Ordered Quantity:{Ordered_quantity}
      Remaining Stocks:{Product_stock}-{Ordered_quantity} ={Remaining_stocks}
      """)

print("---------------------------------------------------------------------------------------------")

print("TASK 3")

print("Banking Application")
name="HDFC"
Account_number="00073237297543"
Customer_name="Ritika Naik"
Mobile_no=70286428742
Account_balance=50000
print(f"""
               {name}
            Banking Details
      Accounr Number:{Account_number}
      Customer Name:{Customer_name}
      Mobile Number:{Mobile_no}
      Account Balance:{Account_balance}
      """)


print("Invalid Identifier are")
print("1.1name")
print("We do not start the variable from number")

print("2.first-name")
print("We do not apply '-' between two variable we use '_'")

print("-----------------------------------------------------------------------------------------------")


print("TASK 4")

print("Find an Error")
print("1.class='Python'")
print("It's an error because class is an pre-defined keyword and are used in OOPs not cannot be used as variable name")

print("\n")
print("2.for=10")
print("It's an Error because the for is also an keyword and are used in loop creation not as a variable name")

print("\n")
print("3.if='Admin'")
print("It's an Error because if is an keyword and are used in conditional statement not as a variable name")

print("\n")
print("Correct Identifier")
course_name="Python"  
user_count=10  
role="Admin"
print(f"""
         Course name:{course_name}
         User count:{user_count}
         Role:{role}
         """)
         
print("--------------------------------------------------------------------------------------------------------")

print("TASK 5")

print("Online Movie Ticket Booking")
name="INOX"
customer_name="Shiya"
ticket_booking="INOX"
movie_name="Leo"
ticket_price=250
no_of_tickets=5
Total_tickets_price=(ticket_price)*(no_of_tickets)
print(f"""
              {name}
           Ticket Details
        Customer Name:{customer_name}
        Ticket_booking:{ticket_booking}
        Movie_name:{movie_name}
        Ticket_price:{ticket_price}
        Total tickets price:{ticket_price}*{no_of_tickets}={Total_tickets_price}
        """)

print("-----------------------------------------------------------------------------------------------------------")

print("TASK 6")

warehouse_details="Warehouse Inventory"
Items_available=500
Sold_items=100
Remaining_stock=(Items_available)-(Sold_items)
print(f"""
      {warehouse_details}
        Warehouse Details
      Items availabe:{Items_available}
      Sold Items:{Sold_items}
      Remaining Stocks arr:{Items_available}-{Sold_items}={Remaining_stock}
      """)

print("-------------------------------------------------------------------------------------------------------------")

print("TASK 7")

print("Petrol Pump Billing")
name="Indian Oil"
customer_name="Roshan"
petrol_purchase=12.5
price_per_litre=105.50
total_bill_amount=(petrol_purchase)*(price_per_litre)
print(f"""
         {name}
        Petol Pump Details
        Customer name:{customer_name}
        Petrol_purchase:{petrol_purchase}
        Price Perlitre:{price_per_litre}
        Total Billing:{petrol_purchase}*{price_per_litre}={total_bill_amount}
        """)

print("-------------------------------------------------------------------------------------------------------------")

print("TASK 8")

print("Student Percentage Calculator")
name="Jay Hind High School"
student_name="Roshini"
marks_obtained_in_subject="Python"
student_obtained_marks=455
Total_marks=500
Percentage=(student_obtained_marks)/(Total_marks)
print(f"""
           {name}
        Student Name:{student_name}
        Marks Obtained in Subject:{marks_obtained_in_subject}
        Student Obtained Marks:{student_obtained_marks}
        Total Marks are:{Total_marks}
        Percentage:{student_obtained_marks}/{Total_marks}={Percentage}%
""")

print("----------------------------------------------------------------------------------------------------------------")

print("TASK 9")

print("Electrical Engineering Application")

name="Tata Comapany"
voltage=220+50j
print("Voltage type is",type(voltage))
current=10+5j
print("Current Type is",type(current))
calculate=(voltage)+(current)
print(f"""
        {name}
      Voltage:{voltage}
      Current:{current}
      Total:{voltage}+{current}={calculate}
      """)

print("-------------------------------------------------------------------------------------------------------------------")

print("TASK 10")

print("Signal Processing System")
signal1=5+3j
signal2=2+7j
calculate=(signal1)+(signal2)
print("Signal1 number is: 5+3j")
print("Signal2 number is: 2+7j")
print("The Two Complex Signal Number are:",calculate)

print("--------------------------------------------------------------------------------------------------------------------")

print("TASK 11")

print("Online Shopping Discount System")
name="Amazon"
customer_name="Rohit"
product_name="Cup Set"
product_price="2500"
discount=10
int1=int(product_price)
print("Converted from String to Inttger",int1)
Total_price=(int1)-(discount)
print(f"""
           {name}
    Customer name:{customer_name}
    Product name:{product_name}
    Product price:{product_price}
    Discount:{discount}
    Total price:{int1}-{discount}={Total_price}

""")

print("----------------------------------------------------------------------------------------------------------------------")

print("TASK 12")

print("ATM Withdrawal System")
name="AXIS Bank"
customer_name="Mrunal"
amount_entered="5000"
float1=float(amount_entered)
print(f"""
         {name}
    Customer name:{customer_name}
    Amount entered:{amount_entered}
    Amount in float:{float1}
    """)

print("----------------------------------------------------------------------------------------------------------------------")

print("TASK 13")

print("Sensor Monitoring System")
name="AC"
temp=35.89
int2=int(temp)
print("Tempersture of",name,"is",int2)

print("--------------------------------------------------------------------------------------------------------------------------")

print("TASK 14")

print("Student Registration Form")
student_name=input("Enter Student Name:")
student_age=int(input("Enter Age:"))
student_course=input("Enter Course Name:")
print(f"""
        Student Name:{student_name}
        Student Age:{student_age}
        Student Course:{student_course}
        """)

print("--------------------------------------------------------------------------------------------------------------------------")

print("TASK 15")

print("Hospital Management System")
patient_id=input("Enter Patient Id:")
patient_name=input("Enter Patient Name:")
patient_age=input("Enter Patient Age:")
patient_weight=input("Enter Weight:")
print(f"""
        Patient Id:{patient_id}
        Patient Name:{patient_name}
        Patient Age:{patient_age}
        Patient Weight:{patient_weight}
        """)

print("---------------------------------------------------------------------------------------------------------------------------")

print("TASK 16")

print("Food Delivery Application")
customer_name=input("Enter Customer Name:")
food_item=input("Enter Food Item:")
Quantity=int(input("Enter Quantity:"))
price=int(input("Enter price"))
Total_Bill=(Quantity)+(price)
print(f"""
        Customer Name:{customer_name}
        Food Items:{food_item}
        Quantity:{Quantity}
        Price:{price}
        Total Bill:{Quantity}+{price}={Total_Bill}
        
        """)

print("------------------------------------------------------------------------------------------------------------------------------")

print("TASK 17")

print("Employee Payroll System")
employee_name=input("Enter Employee Name:")
basic_salary=int(input("Enter Basic Salary:"))
bonus=int(input("Enter Bouns:"))
tax=int(input("Enter tax:"))
Net=(basic_salary)+(bonus)-(tax)
print(f"""
         Employee Name:{employee_name}
         Bonus:{bonus}
         Tax:{tax}
         Net:{basic_salary}+{bonus}-{tax}={Net}
         """)

print("-----------------------------------------------------------------------------------------------------------------------------------")

print("TASK 18")

print("Bank Account Opening System")
account_details="Kotak Bank"
account_number=int(input("Enter account number"))
customer_name=input("Enter Customer Name:")
phone_no=int(input("Enter Phone Number:"))
deposite_amount=int(input("Enter the deposite amount"))
print(f"""
       {account_details}
    Account Number:{account_number}
    Customer Name:{customer_name}
    Phone Number:{phone_no}
    Deposite Amount:{deposite_amount}
    """)

print("-------------------------------------------------------------------------------------------------------------------------------------")
     
print("TASK 19")

print("Smart Electricity Bill Generator")
customer_id=int(input("Enter Customer Id:"))
customer_name=input("Enter Customer Name:")
unit_consumed=float(input("Enter Unit Consumed:"))
rate_per_unit=float(input("Enter Rate Per Unit"))
bill_amount=(unit_consumed)*(rate_per_unit)
gst=(bill_amount)*0.18
final_bill=(bill_amount)+(gst)
print(f"""
       Customer Id:{customer_id}
       Customer Name:{customer_name}
       Unit Consumed:{unit_consumed}
       Rate Per Unit:{rate_per_unit}
       Bill Amount:{unit_consumed}*{rate_per_unit}={bill_amount}
       GST:{bill_amount}*0.18={gst}
       Final Bill:{bill_amount}+{gst}={final_bill}
       """)

print("-----------------------------------------------------------------------------------------------------------------------------------")

print("TASk 20")

print("Online Course Enrollment Portal")
student_id=int(input("Enter Student Id:"))
print("Student Id Type is:",type(student_id))
student_name=input("Enter Student Name")
print("Student Name type is:",type(student_name))
course_name=input("Enter the course Name:")
print("Student Course type is:",type(course_name))
course_fee=int(input("Enter Course Fees"))
print("Student Course fee type is:",type(course_fee))
gst_per=int(input("Enter gst percentage:"))
gst_amount=(course_fee)*(gst_per/100)
total_fee=(course_fee)+(gst_amount)
print(f"""
    Student Id:{student_id}
    Student Name:{student_name}
    Course Name:{course_name}
    Course fee:{course_fee}
    Gst Percentage:{gst_per}
    Gst Amount:{course_fee}*{gst_per/100}={gst_amount}
    Total Fees:{course_fee}+{gst_amount}={total_fee}
    """)

