libraries=[]
def Add_Book():
    print("---------Add Book Details----------")
    book_id = int(input("Enter the book id : "))
    book_name = input("Enter the book name : ")
    author_name = input("Enter the author name : ")
    book_status = input("Enter th book (Available) or not : ")

    library=[
            book_id,
            book_name,
            author_name,
            book_status
    ]

    libraries.append(library)

def View_Book():
    print("-----------View Book Details-----------")
    for library in libraries:
        book_id = library[0]
        book_name = library[1]
        author_name = library[2]
        book_status = library[3]

        print("Book Id : " , book_id)
        print("Book Name : " , book_name)
        print("Author Name : " , author_name)
        print("Book Staus : ", book_status)
        print("----------------------------------------------")

def Search():
    print("----------Search Books----------")
    bid = int(input("Enter the book id : "))
    found=False

    for library in libraries:
        if library[0] == bid:
            book_id = library[0]
            book_name = library[1]
            author_name = library[2]
            book_status = library[3]

            print("The Book Details has been found")
            print("-----------------------------------------")
            print("Book Id : " , book_id)
            print("Book Name : " , book_name)
            print("Author Name : " , author_name)
            print("Book Staus : ", book_status)


            found = True
            break
    if found == False:
        print("Book not found")

def Update():
    print("----------Update Book--------")
    bid1 = int(input("Enter the book id : "))
    found = False

    for library in libraries:
        if library[0] == bid1:
            book_id = library[0]
            book_name = library[1]
            author_name = library[2]
            book_status = library[3]

            print("Book has been found")
            print("---------------------------------")
            print("Book Id : " , book_id)
            print("Book Name : " , book_name)
            print("Author Name : " , author_name)
            print("Book Staus : ", book_status)

            print("-------Updated Book Details---------")
            update_book_name = input("Enter the book name : ")
            update_author_name = input("Enter the author name : ")
            update_book_status = input("Enter the book status : ")

    
            library[1] = update_book_name
            library[2] = update_author_name
            library[3] = update_book_status

        
            book_name = library[1]
            author_name = library[2]
            book_status = library[3]

            print("-----Books Updated Successfully-----")
            print("Book Name : " , update_book_name)
            print("Author Name : " , update_author_name)
            print("Book Status : ", update_book_status)


            found = True
            break

    if found == False:
        print("Book not found")

def Delete():
    print("-------Delete Book Details------")
    delete_books = int(input("Enter the book id : "))
    found = False

    for library in libraries:
        if library[0] == delete_books:
            print("Books has been found")
            libraries.remove(library)
            found = True
            print("The books record has been deleted successfully")
            break

    if found == False:
        print("Books not found")

while True:
    print(f"""
                    -----Library Management System------
            1. Add Book Details.
            2. View all books.
            3. Search Books.
            4. Update Books.
            5. Delete Book Details.
            6. Exit
        """)
    choice = int(input("Enter the Choice : "))
    if choice == 1:
        Add_Book()

    elif choice == 2:
        View_Book()

    elif choice == 3:
        Search()

    elif choice == 4:
        Update()

    elif choice == 5:
        Delete()

    elif choice == 6:
        print("Thank You and Visit Again")
        break

    else:
        print("Invalid Choice")

        



            