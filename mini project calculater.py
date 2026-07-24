history = []
while True :
    print("\t\t\tcalculator app")

    print("""
            1. Addition
            2. substraction
            3. Multiplication
            4. Division
            5. Floor Division
            6. Modulus
            7. Exponational
            8. Exist
    """)

    ch = int(input("Enter Your Choice : "))

    if ch in [1,2,3,4,5,6,7,8] :

            if ch == 8 :  
                if history :
                    print("\t\t\tclaculator History")
                    s = 1
                    for his in history :
                        print(f"{s} . {his}")
                        s+=1
                print("\t\t\tVisit  Again !!!!!")
                break

            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))

            if ch == 1 :
                add = num1 + num2 
                msg = f"Addition of {num1} + {num2} = {add}"
                print(msg)

            elif ch == 2 :
                sub = num1 - num2 
                msg = f"Subtraction of {num1} - {num2} = {sub}" 
                print(msg)
            elif ch == 3 :
                mul = num1 * num2 
                msg = f"Multiplication of {num1} * {num2} = {mul}" 
                print(msg)

            elif ch == 4 :
                if num2 > 0:
                    div = num1 / num2 
                    msg = f"Division of {num1} / {num2} = {div}" 
                    print(msg)

                else :
                    msg = "Enter num2 > 0(division)"
                    print(msg)
                    continue


            elif ch == 5 :
                if num2 > 0:
                    fdiv = num1 // num2 
                    msg = f"floor division of {num1} // {num2} = {fdiv}"
                    print(msg)

                else :
                    msg = "Enter num2 > 0(floor division)"
                    print(msg)

            elif ch == 6  :
                if num2 > 0:
                    mod = num1 % num2 
                    msg = f"Modlus of {num1} % {num2} = {mod}" 
                    print(msg)

                else :
                    msg = "Enter num2 > 0(Modlus)"
                    print(msg)

            elif ch == 7 :
                if num2 > 0 :
                    epo = num1 ** num2 
                    msg = f"Exponatioal of {num1} ** {num2} = {epo}"
                    print(msg)
        
                else :
                    msg = "Enter num2 > 0(Exponantioal)"
                    print(msg)

            history.append(msg)
    else : 
        print("Invalid input please enter operation (0 to 8)")
        continue


