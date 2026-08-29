students=[]
while True:

    print(f"""---------Student Management System-------------
        1. Add Student Details.
        2. View Student Details.
        3. Search Student Details.
        4. Update Student Details.
        5. Delete Student Details.
        6. Exit.
    """)

    choice = int(input("Enter the choice : "))
    

    if choice == 1:
        print("------Add Student Details-----")

        roll_no = int(input("Enter the Roll No : "))
        name = input("Enter the name : ")
        python_marks = int(input("Enter the python marks : "))
        dbms_marks = int(input("Enter the DBMS marks : "))
        java_marks = int(input("Enter the java marks : "))

        total_marks = python_marks + dbms_marks + java_marks
        print("Total Marks is : " ,total_marks)

        percentage = (total_marks/300)*100
        print("Percentage is : " ,percentage)

        if percentage >= 90:
            print("A+ Grade")
        elif percentage >= 80:
            print("A Grade")
        elif percentage >= 70:
            print("B Grade")
        elif percentage >= 60:
            print("C Grade")
        elif percentage >= 50:
            print("D Grade")
        else:
            print("Fail")

        student=[
            roll_no,
            name,
            python_marks,
            dbms_marks,
            java_marks
        ]
        students.append(student)
    

    elif choice == 2:

        print("---------View Details--------")
        for student in students:
            roll_no = student[0]
            name = student[1]
            python_marks = student[2]
            dbms_marks = student[3]
            java_marks = student[4]

            print("Roll Number : ", roll_no)
            print("Student Name  : ", name)
            print("Python Marks is : ", python_marks)
            print("DBMS marks is : ", dbms_marks)
            print("Java marks is : ", java_marks)
            print("------------------------------------------------")

    elif choice == 3:
        print("---------Search student Details---------")
        search_roll = int(input("Enter the roll number to search : "))
        found = False

        for student in students:
            if student[0] == search_roll:
                roll_no = student[0]
                name = student[1]
                python_marks = student[2]
                dbms_marks = student[3]
                java_marks = student[4]

                print("Roll number has been matched this is the details of student.")
                print("Roll Number : ", roll_no)
                print("Student Name  : ", name)
                print("Python Marks is : ", python_marks)
                print("DBMS marks is : ", dbms_marks)
                print("Java marks is : ", java_marks)
                print("------------------------------------------------")
                
                found = True
                break  

        if found == False:
            print("The student details not found.")

    elif choice == 4:
        print("----------Update Student Details----------")
        search_student = int(input("Enter the roll no : "))
        found=False

        for student in students:
            if student[0] == search_student:

                roll_no = student[0]
                name = student[1]
                python_marks = student[2]
                dbms_marks = student[3]
                java_marks = student[4]

                print("Roll number has found")
                print("----------------------------------")
                print("Roll Number : ", roll_no)
                print("Student Name  : ", name)
                print("Python Marks is : ", python_marks)
                print("DBMS marks is : ", dbms_marks)
                print("Java marks is : ", java_marks)
                print("------------------------------------------------")
                

                print("--------Update the student Details-------")
                update_name = input("Enter the name : ")
                update_python_marks = int(input("Enter the python marks : "))
                update_dbms_marks = int(input("Enter the DBMS marks : "))
                update_java_marks = int(input("Enter the java marks : "))

                student[1] = update_name
                student[2] = update_python_marks
                student[3] = update_dbms_marks
                student[4] = update_java_marks

                roll_no = student[0]
                name = student[1]
                python_marks = student[2]
                dbms_marks = student[3]
                java_marks = student[4]


                print("------------Student's Updated Details-----------")
                print("Roll Number : ", roll_no)
                print("Student Name  : ", name)
                print("Python Marks is : ", python_marks)
                print("DBMS marks is : ", dbms_marks)
                print("Java marks is : ", java_marks)
                print("------------------------------------------------")
                
                found = True
                break

        if found==False:
            print("Student not found")

    elif choice == 5: 
        print("-----------Delete Student Details-----------")
        delete_roll_no = int(input("Enter the roll no that has to be delete : "))
        found = False

        for student in students:
            if student[0] == delete_roll_no:
                print("Roll number has been found")
                students.remove(student)
                found = True
                print("The student record has been deleted")
                break

        if found == False:
            print("Student not found.")

    elif choice == 6:
        print("---------Thank you and Visit Again----------")
        break

    else:
        print("Invalid choice print the valid choice")





            



