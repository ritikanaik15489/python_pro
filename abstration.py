
# from abc import ABC,abstractmethod
# class Demo1(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Display_details(self):
#         print(f"Student name is : {self.name} , Student age : {self.age}")
# d1=Demo1("Ritika",20)
# d1.Display_details()

# this is an abstract class 
# we can create the object of abstract class when no abstract method is present 

# ---------------------------------------------------------------------------------------------------------

# from abc import ABC,abstractmethod
# class Demo1(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @abstractmethod
#     def Display_details(self):
#         print(f"Student name is : {self.name} , Student age : {self.age}")
# d1=Demo1("Ritika",20)
# d1.Display_details()
# we cannot able to create the abstract object
# TypeError: Can't instantiate abstract class Demo1 without an implementation for abstract method 'Display_details'

# =--------------------------------------------------------------------------------------------------------


# from abc import ABC,abstractmethod
# class Demo1(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @abstractmethod
#     def Display_details(self):
#         print(f"Student name is : {self.name} , Student age : {self.age}")

#     def _showInfo(self):
#         print(f"Student name is : {self.name}")

#     def __add__(self, other):
#         total_age=self.age+other.age
#         print(total_age)

# d1=Demo1("Ritika",20)
# d1.Display_details()

# class Demo3(Demo1):
#     def __init__(self, name, age):
#         super().__init__(name, age)

#     def Display_details(self):
#         return super().Display_details()

# cl = Demo3("Roshani", 30)
# cl._showInfo()

# when we are inheriting the demo1 to demo2 has to hav same name of display_details rather than other name
# this is an is-a relationship
# in this we have perform overall the oops concept and the screenshot has been taken.
# ---------------------------------------------------------------------------------------------------------------
 

