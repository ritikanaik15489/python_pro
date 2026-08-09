# class Parent:
#     pcv="Parent"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def parent_info(self):
#         print(f"Parent name : {self.name} and age is : {self.age}")
#     def Addition(self,num1,num2):
#         add=num1+num2
#         print(f"Addition of {num1} and {num2} is : {add}")
# p1=Parent("Pratik",89)
# p1.Addition(10,20)
# p1.parent_info()
# self.name or self.n can also pass because its an variable self.name=name the =name has to same beacuse the parametre has passed by name


# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def child_info(self):
#             print(f"Parent name : {self.name} and age is : {self.age}")
# c1=Child("Mahima",30)
# c1.parent_info()
# name and age get access in def beause it inherits the parent class properties 


# class Child(Parent):
#     def __init__(self, name, age, city):
#         super().__init__(name, age)
#         self.city=city
#         super().parent_info()
#         super().Addition(9,8)
#     def child_info(self):
#             print(f"Parent name : {self.name} and age is : {self.age} , City is {self.city}")
# c1=Child("Mahima",30,"Pune")
# c1.parent_info()
# c1.child_info()

# in child class we can add the city,address or anything else 
# through using the super().parentinfo and addition we can access the parent class properties

# class Child(Parent):
#     def __init__(self, name, age, city):
#         super().__init__(name, age)
#         self.city=city
#         super().parent_info()
#         super().Addition(9,8)
#         # print(super().name)
#         # or print(super.name)
#         # or print(super.self.name)
#         # print(super().age)
#         print(super().pcv)
#     def child_info(self):
#             print(f"Parent name : {self.name} and age is : {self.age} , City is {self.city}")
# c1=Child("Mahima",30,"Pune")
# c1.parent_info()
# c1.child_info()

# we cannot able to access the name and age by the super keyeword that's why in parent class we have use the variable with pcv="parent" to accses the parenent class

# ---------------------------------------------------------------------------------------------------------------------------
# class Parent:
#     pcv="Parent"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def parent_info(self):
#         print(f"Parent name : {self.name} and age is : {self.age}")
#     def Addition(self,num1,num2):
#         add=num1+num2
#         print(f"Addition of {num1} and {num2} is : {add}")
#     @staticmethod
#     def StaticMethod(num3,num4):
#         print(f"Addition of {num3} and {num4} is :{num3*num4}")
# p=Parent("Ritika",34)
# p.parent_info()
# p.Addition(23,6)
# p.StaticMethod(5,7)


# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print(super().pcv)
#         super().StaticMethod(3,5)
#     def child_info(self):
#         print(f"parent name {self.name} , parent age {self.age}")

# c=Child("Mahima",23)
# c.Addition()
# c.StaticMethod(7,8)

# class Child1:
#     def __init__(self,name,age):
#         Parent("MAhima",23).__init__(name,age)
        # if we create another child class then with __init__ then they are giving the  super().__init__(name, age) instead of this it is passing the pass
        # that's why this way we can call the parent class name and age
        # Parent("MAhima",23).parent_info()
        # Parent("MAhima",23).Addition(6,8)
        # Parent("MAhima",23).StaticMethod(8,10)
        # print(Parent("MAhima",23).pcv) 
        # pcv is an variable that's why has to be put in print()

# c1=Child1("MAhima",23)
# has  to pass th value because of constructor 

# ----------------------------------------------------------------------------------------------------------------------------
class Parent:
    pcv="Parent"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def parent_info(self):
        print(f"Parent name : {self.name} and age is : {self.age}")
    def Addition(self,num1,num2):
        add=num1+num2
        print(f"Addition of {num1} and {num2} is : {add}")
    @staticmethod
    def StaticMethod(num3,num4):
        print(f"Addition of {num3} and {num4} is :{num3*num4}")
p=Parent("Ritika",34)
# p.parent_info()
# p.Addition(23,6)
# p.StaticMethod(5,7)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(super().pcv)
        super().StaticMethod(3,5)
    def child_info(self):
        print(f"parent name {self.name} , parent age {self.age}")
#  c=Child("Mahima",23)
# c.Addition()
# c.StaticMethod(7,8)


class Child1:
    def __init__(self,name,age):
        # Parent("MAhima",23).__init__(name,age)
        # Parent("MAhima",23).parent_info()
        # Parent("MAhima",23).Addition(6,8)
        # Parent("MAhima",23).StaticMethod(8,10)
        # print(Parent("MAhima",23).pcv) 
        # pcv is an variable that's why has to be put in print()

        # p.parent_info()
        # p.StaticMethod(8,9)
        # p.Addition(7,9)
        # print(p.pcv)
        # we can call the parent properties through this also without the super()

        p.parent_info()
        p.StaticMethod(8,9)
        p.Addition(7,9)
        print(p.pcv)
        print(p.name)

c1=Child1("MAhima",23)


