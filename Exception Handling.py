# num1=10
# num2=0
# print(num1/num2)
# print("operation success!!")

# because of this program writen the print("operation sucess ") no able to print an output.

# Exception hnadling i used where you are ablr to knowing where the error will get occur then only put an ecxception don't provide the excepton to whole code

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# num1=10
# num2=0
# try:
#     print(num1/num2)
# except Exception as e:
#     print(e)
# print("operation success")
# now in this code the exception and the print("operation sucees") also getting print
# Exception it is an class
# Paren class of exception is baseException

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# num1=10
# num2=56
# try:
#     print(num1/num2)
# except Exception as e:
#     print(e)
# else:
#     print("operation success")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


# num1=10
# num2=56
# try:
#     print(num1/num2)
# except Exception as e:
#     print(e)
# else:
#     print("operation success")
# finally:
#     print("Welcome")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# num1=18
# num2=int(input("Enter the age : ")) it will give output but it is not correct it will give an error as value error
# try:
#     num2 = int(input("Enter the age : "))
#     if num2>=18:
#         print("Eligible")
#     else:
#         raise Exception
# except Exception as e:
#     print(e)
# we can apply mutliple execpt block in code.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

l1=[10,20,30]
try:
    print(l1.remove(45))
except IndexError as e:
    print(e)
except ValueError as f:
    f="Value not found"
    print(f)
print("Operation succesd")