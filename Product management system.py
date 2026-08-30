product = []
def Add_Products():
    print("--------Add Product Details-------")

    try:
        product_id = int(input("Enter the product id : "))
        product_name = input("Enter the product name : ")
        product_price = int(input("Enter the product price : "))
        product_quantity = int(input("Enter the product quantity : "))

        products=[
        product_id,
        product_name,
        product_price,
        product_quantity
        ]
        product.append(products)

    except ValueError:
        print("Invalid input. Please enter a valid Product ID.")

def View_Products():
    print("--------View Product Details--------")

    for products in product :

        product_id = products[0]
        product_name = products[1]
        product_price = products[2]
        product_quantity = products[3]
            
        print("Product id is : " , product_id)
        print("Product Name is : " , product_name)
        print("Product Price is : ", product_price)
        print("Product quantity is : ", product_quantity)
        print("----------------------------------------------------")


def Search_Products():
    print("----------Search Product--------")

    try:
        pid = int(input("Enter the product id : "))
        found = False

        for products in product:
            if products[0] == pid:
                product_id = products[0]
                product_name = products[1]
                product_price = products[2]
                product_quantity = products[3]

                print("-----------Product Details Found-------------")
                print("Product id is : " , product_id)
                print("Product Name is : " , product_name)
                print("Product Price is : ", product_price)
                print("Product quantity is : ", product_quantity)
                
                found = True
                break

        if found == False:
            print("Products not found")

    except ValueError:
      print("Invalid input. Please enter a valid Product ID.")

def Update_Products():

    print("---------Update Product Deatails---------")

    try:
        pid1 = int(input("Enter the product id : "))
        found = False

        for products in product:
            if products[0] == pid1:
                product_id = products[0]
                product_name = products[1]
                product_price = products[2]
                product_quantity = products[3]
                
                print("-----------Product Details Found-------------")
                print("Product id is : " , product_id)
                print("Product Name is : " , product_name)
                print("Product Price is : ", product_price)
                print("Product quantity is : ", product_quantity)


                print("-------Update the Product Details-------")
                update_product_name = input("Enter the product name : ")
                update_product_price = int(input("Enter the product price : "))
                update_product_quantity = int(input("Enter the product quantity : "))

                products[1] = update_product_name
                products[2] = update_product_price
                products[3] = update_product_quantity

                print("Product updated successfully")
                                
                found = True
                break

        if found == False:
            print("Products not found")

    except ValueError:
        print("Invalid input. Please enter a valid Product ID.")

def Delete_Product():
    delete_product = int(input("Enter the product id : "))
    found = False

    for products in product:
        if products[0] == delete_product:
            print("The Product has been removed.")
            product.remove(products)
            found = True 
            break

    if found == False:
        print("Products not found")
      
print(f"""
           ------------Product Management System---------
           1. Add Products.
           2. View Products.
           3. Search Products.
           4. Update Products.
           5. Delete Products.
           6. Exit.

""")
choice = int(input("Enter the choice : "))

if choice == 1:
    Add_Products()

elif choice == 2:
    View_Products()

elif choice == 3:
    Search_Products()

elif choice == 4:
    Update_Products()

elif choice == 5:
    Delete_Product()

elif choice == 6:
    print("Thank you and visit again")

