import csv


# READ PRODUCTS CSV

products = []

csv_file_path = "data/products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

menu = """
    Hi.

    Welcome to the products app.

    There are 100 products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))



# example of manipulating/changing the products list
example_new_product = {"id": 100, "name": "New Item", "aisle": "snacks", "department": "snacks", "price":1.99}
products.append(example_new_product)



def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    Product_aisle = input("aisle is:")
    product_department = input ("department is:")
    product_price = input ("price is:")
    new_product = {
    
    }




with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)

#chosen_operation = input(menu)
#chosen_operation = chosen_operation.title()
#
#def list_products():
#    print("LISTING PRODUCTS")
#
#def show_product():
#    print("SHOWING A PRODUCT")
#
#def create_product():
#    print("CREATING A PRODUCT")
#
#def update_product():
#    print("UPDATING A PRODUCT")
#
#def destroy_product():
#    print("DESTROYING A PRODUCT")
#
#if chosen_operation.title() == "List":
#elif chosen_operation.title() == "Show":
#elif chosen_operation.title() == "Create":
#elif chosen_operation.title() == "Update":
#elif chosen_operation.title() == "Destroy":
#else:print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
