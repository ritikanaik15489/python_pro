# Module:-collection of method,function,class,variable.
# modules mean single .py file

# Package :- collection of modules means mutiple.py file.
            # identify using __init__.py file this file will be empty.

# Types of modules.
# 1.user-define
# 2.pre-defined built in(csv,os,keyword,pathlib,map,abc,etc.)
# 3.third-party(pandas,matplotlib,numpy)


# 1.Pre-defined 

# import math
# # print(math.ceil(10.5)) givies the nearest number of the given value.
# print(math.floor(10.2))
# print(math.factorial(20))

# --------------------------------------------------------------------------------

# import random as r
# print(r.randint(0,9),r.randint(0,9),r.randint(0,9),r.randint(0,9)) it will give the random number this is help for otp purpose.

# ----------------------------------------------------------------------------------

# import random as r
# import string as s
# print(r.choice(s.ascii_letters),r.choice(s.ascii_letters),r.choice(s.ascii_letters),r.choice(s.ascii_letters)) for random letters.

# print(r.choice(s.ascii_letters),r.randint(0,9),r.choice(s.ascii_letters),r.randint(0,9),r.choice(s.ascii_letters),r.randint(0,9),r.choice(s.ascii_letters),r.randint(0,9)) in this it used to perform both random alphabet and number 

# ------------------------------------------------------------------------------------

# Using the deque 

# from collections import deque
# d1=deque([10,20,30])
# d1.rotate(2)
# d1.rotate(5)
# d1.rotate(4)
# the rotate is used to rotate the list as per provided value in rotate.It will roatate from the right side.
# print(d1)

# -------------------------------------------------------------------------------------------

# from collections import deque

# d2={}
# print(d2['name'])It will give error as key error becuase the name doest not exist in dict.

# from collections import *
# d3=defaultdict(int)
# d3=['name']
# print(d3)  
# It will get an output as name without any keyerror because of defaultdict .In first case it was giving an error now it will not give an error.

# ---------------------------------------------------------------------------------------

# character count
# from collections import *
# str1="xfchgvjbngfchvjbknrytfghjlk"
# d1={}
# for i in str1:
#     d1[i]=str1.count(i)
# # print(d1)
# print(Counter(str1))  

# -----------------------------------------------------------------------------------------


# Orderdict,namethetuple,chainmap,

# from collections import OrderedDict
# data={"apple":4,"grapes":8,"banana":10,"mango":3}
# sequence=OrderedDict(sorted(data.items()))
# print(sequence)

# from collections import ChainMap
# data={"theme":"dark","font":"Calibria"}
# data1={"fruit":"sweet","user":"guest"}
# sequence=ChainMap(data,data1)
# print(sequence["fruit"])
# print(sequence["user"])

# from collections import namedtuple
# plot=namedtuple('Point',['x','y'])
# pt=plot(10,20)
# print(pt.x)
# print(pt.y)


