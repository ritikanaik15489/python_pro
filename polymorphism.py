# class Parent:
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         print(self.name, " " ,self.age)

# p1=Parent("Adi",78)

# p2=Parent("Roshani") not support constructor overloading beacuse of interpreter
# -------------------------------------------------------------------------------------------

# class Parent1:
#     def Square(self,num1):
#         print(num1*num1)

#     def Square(self,num1,num2):
#             print(num1**num2)
# p2=Parent1()
# p2.Square(3,3)
# p2.Square(3) cannot support the method overloading 

# ----------------------------------------------------------------------------------------------

# class Student_info:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Student_info(self):
#          print(f"Student name :{self.name} , student age : {self.age}")
# s1=Student_info("Pranav",34)
# s1.Student_info()

# s2=Student_info("Aditiya",90)
# s2.Student_info()

# print(s1.age+s2.age)
# addition of age
# we can able to perforn an object operation 

# ------------------------------------------------------------------------------------------------
          
class Student_info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Student_info(self):
         print(f"Student name :{self.name} , student age : {self.age}")
    def __add__(self, other):
         agesum=self.age+other.age 
         print(agesum)
    def __div___(self, other):
             agesum=self.age/other.age 
             print(agesum)
s1=Student_info("Pranav",34)
s1.Student_info()

s2=Student_info("Aditiya",90)
s2.Student_info()

s1+s2
s1.__div___(s2)
# this is an operator overloading we support operator oveloading
# print(s1.age+s2.age) can be done by constructor for performing the operations
# we can perform __add___ with string and number

# -------------------------------------------------------------------------------------------------

class IPL:
     def Player(self):
          print("IPL player method")
class WPL(IPL):
     def Player(self):
               print("WPL player method")
w1=WPL()
w1.Player()
# is the parent ansd child class has both same method so it will call the child class method instead of parent cals method
# this is an method overrriding 

