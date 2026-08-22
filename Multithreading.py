# def square():
#     sq=2*2
#     print(sq)
# def cube():
#     cub=2**3
#     print(cub)

# s=square()
# c=cube()

# -----------------------------------------------------------------------------

# Using the time 

# import time
# def square():
#     sq=2*2
#     print("Square function start")
#     time.sleep(6)
#     print(sq)
# def cube():
#     cub=2**3
#     print("Cube function start")
#     time.sleep(4)
#     print(cub)
# s=square()
# c=cube()

# The output is getting exeuting line by line due to giving the time the 1st as be run as cube and then square but it will get 1st run as square then cube according to the seounds passed.
# This is getting executed parellely
# -----------------------------------------------------------------------------

# import time
# import threading
# def square():
#     sq=2*2
#     print("Square function start")
#     time.sleep(6)
#     print(sq)
# def cube():
#     cub=2**3
#     print("Cube function start")
#     time.sleep(4)
#     print(cub)

# s1=threading.Thread(target=square)
# c1=threading.Thread(target=cube)    #/*We have just created the thread*/

# s1.start()         #Now the thread has beeen started
# c1.start()

# Now in this the cube will get first executed then the square will get executed.

# ------------------------------------------------------------------------------------

# By passing an arguments.

# import time
# import threading
# def square(num1):
#     sq=num1*2
#     print("Square function start")
#     time.sleep(6)
#     print(sq)
# def cube(num2):
#     cub=num2**3
#     print("Cube function start")
#     time.sleep(4)
#     print(cub)

# s1=threading.Thread(target=square,args=[10])
# c1=threading.Thread(target=cube,args=[12]) 

# s1.start()         #Now the thread has beeen started
# c1.start()

# print("operation succesd")

# In this the opertion successd also given output within the print of square and cube function start.
# So becuause of this the thread has be given as closing also.

# ----------------------------------------------------------------------------------------

# By join function to close the thread.

# import time
# import threading
# def square(num1):
#     sq=num1*2
#     print("Square function start")
#     time.sleep(6)
#     print(sq)
# def cube(num2):
#     cub=num2**3
#     print("Cube function start")
#     time.sleep(4)
#     print(cub)

# s1=threading.Thread(target=square,args=[10])
# c1=threading.Thread(target=cube,args=[12]) 

# s1.start()         #Now the thread has beeen started
# c1.start()

# s1.join()
# c1.join()

# print("operation succesd")

# Now the operaton successd will print after the all execution.

# ------------------------------------------------------------------------------------------

# import time
# import threading
# def square(num1):
#     sq=num1*2
#     print("Square function start")
#     time.sleep(1)
#     print(sq)
# def cube(num2):
#     cub=num2**3
#     print("Cube function start")
#     time.sleep(1)
#     print(cub)

# s1=threading.Thread(target=square,args=[10])
# c1=threading.Thread(target=cube,args=[12]) 

# s1.start()         #Now the thread has beeen started

# print(s1.getName)

# s1.join()

# Output
# Square function start
# <bound method Thread.getName of <Thread(Thread-1 (square), started 12000)>> Which function the thread is.
# 20

# s1.start()         

# print(s1.getName())  

# s1.join()

# Output
# Square function start
# c:\Python Code\Multithreading.py:143: DeprecationWarning: getName() is deprecated, get the name attribute instead
#   print(s1.getName())
# Thread-1 (square)
# 20


# ------------------------------------------------------------------------------------------------

# Using the ident

# import time
# import threading
# def square(num1):
#     sq=num1*2
#     time.sleep(1)

# s1=threading.Thread(target=square,args=[10])

# s1.start()         #Now the thread has beeen started

# # print(s1.ident)   

# print(s1.native_id)
# s1.join()

# ident It is an id of an thread that is generate in memory.
# native_id is also same as ident.

# ----------------------------------------------------------------------------------------------

# using is_alive

# import time
# import threading
# def square(num1):
#     sq=num1*2
#     time.sleep(1)

# s1=threading.Thread(target=square,args=[10])

# s1.start()
# print(s1.is_alive())
# s1.join()

# is_alive give the output has trur or false it is between the start and join means inside the function which are performing the task that's why it gives true.
# if is placed outside the join function it will give false.
# -------------------------------------------------------------------------------------------

# print(s1.run)
# Do not write inside becuase it will give error instead of after using start in internally run the code so we do not able to writ the run().

# ---------------------------------------------------------------------------------------

# Using set name

import time
import threading
def square(num1):
    sq=num1*2
    time.sleep(1)

s1=threading.Thread(target=square,args=[10])

s1.start()
print(s1.setName("Number Square"))
print(f"After setname : {s1.getName()}")
s1.join()

# Can able to set another name.


