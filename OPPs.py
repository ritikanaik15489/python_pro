# class Demo:
#     print("My First Demo")
# d1=Demo()

# class Demo2():
#     print("Second class")
# d2=Demo()
# # when we inhrits th class we use paranethisis () calling in parenthesis in Demo2()

# class Demo3:
#     def Addition(self,num1,num2):
#         add=num1+num2
#         return add
# d1=Demo3()
# print(d1.Addition(10,20))
# we need to pass the reference variable in the first position of the parameter
# we can create method inside the class
# we need to create the class and the object then only the memory gets alloctaed to that variable \
# self is not a keyword

# class Demo4:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age  
#     def Info(self):
#         return(f"Name is {self.name} , Age is :{self.age}")
# d4=Demo4("Ritika",34)
# # print(d4.__init__("Prtaik",30))
# print(d4.Info())


# ____init___ is an constructor,(self,name,age) is an instance method where the instance variable are stored
# self.name=instance variable right side name is value
# d4.__init__("Pratik",34) we cannot call constructor has an object besause the return type is none

# class Demo4:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age  
#     def Info(self):
#         return(f"Name is {self.name} , Age is :{self.age}")
# d4=Demo4("Ritika",34)
# d4.__init__("Pratik",30)
# print(d4.Info())
# it has get new parmeter we can call d4.__init__("Pratik",30) but cannot print return type is none
  

        #    instance variable/method
# class Demo4:
#     def __init__(self,name,age):
#       self.name=name
#       self.age=age  
#     def Info(self):
#         return(f"Name is {self.name} , Age is :{self.age}")
# d4=Demo4("Ritika",34)
# d4.__init__("Pratik",30)
# print(d4.Info())
# # print(Demo4("Ritika",45).Info()) we can the call by class name with all info of name and age

# print(f"using the object:{d4.name}")  geeting the new d4.__init__("Pratik",30) print name

# print(f"Using the class:{Demo4("MAhima",23).name}") can call class name by only studnt name

# primary instance variable is self.name because of instance variable is instialize and the info() that also an instance variable it is used in info



                        #    class variable/method
# class Demo4:
#     sname = "TKA"
#     add = "Chichwad"

#     def __init__(self,name,age):
#       self.name=name
#       self.age=age  
#     def Info(self):
#         return(f"Name is {self.name} , Age is :{self.age}")
# d4=Demo4("Ritika",34)
# print(f"Using the object:{d4.sname}")
# print(f"USing class name :{Demo4("Siya",8).sname}")
# sname and add are the class variable 

# d5=Demo4()
# print(f"Using the object:{d5.sname}")
# print(f"USing class name :{Demo4().sname}")


# class Demo9:
#     sname = "TKA"
#     add = "Chichwad"

#     def __init__(self,name,age):
#       self.name=name
#       self.age=age  
#     @classmethod
#     def Student_Info(self):
#         return(f"Name is {self.name} , Age is :{self.age}")
# d7=Demo9()
# print(f"using the object {d7.sname}")
# print(f"using the class {Demo9.sname}")
# print(d7.Student_Info())



                    # Local Variable/static 


class Demo8:
    def Addition(self,num1,num2):
        add=num1+num2
        return add
    @staticmethod
    def st_in(name,age):
        print(f"name is {name} and age is :{age}")
# d8=Demo8()
# print(d8.Addition(10,6))
# print(d8.st_in("Ritika",23))


# in static method we did not need to pass the refernce variable as a self because staticmethod is passed
# we cannot call the name or age by the d8.name or by class because staic method is used if self was passed then it will give the o/p by class name and object

class Demo4:
    def __init__(self,name,age):
      self.name=name
      self.age=age  
    def Info(self):
        return(f"Name is {self.name} , Age is :{self.age}")
d2=Demo4("Gayatri",34)
d2.name="mahima"
print(d2.Info())

# manipulation is also done where the object gets new value




