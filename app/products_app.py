import csv
#References an outside CSV file

products = []
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]


def get_product_id(product): return int(product["id"])
def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1



csv_file_path = r"C:\Users\Paloma\Desktop\CRUD Project\CRUDSupermarket\data\products.csv"
#Shows where to find the CSV file


with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #Reading checkpoint
    for row in reader:
        products.append(row)


#Where do we print the menu?
menu = """
    Hi.

    Welcome to the products app.

    There are 100 products originally.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))



# example of manipulating/changing the products list
#example_new_product = {"id": 100, "name": "New Item", "aisle": "snacks", "department": "snacks", "price":1.99}
#products.append(example_new_product)



def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:")
    Product_aisle = input("aisle is:")
    product_department = input ("department is:")
    product_price = input ("price is:")
    new_product = {

    }


def liaison(chosen_operation): # this is a function that links the menu to the actual operations that are defined below.
    if chosen_operation == "List":
        list_products()
    elif chosen_operation == "Show":
        show_product()
    elif chosen_operation == "Create":
        create_product()
    elif chosen_operation == "Update":
        update_product()
    elif chosen_operation == "Destroy":
        destroy_product()
    else:
        print("PLEASE SELECT ONE OF THE FIVE MENU OPTIONS")


def list_products():
    print("LISTING PRODUCTS")
    for product in products:
        print(" + " + product["id"] + product["name"] + product["aisle"] + product["department"] + product["price"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("SHOWING PRODUCT HERE:", product)

    else:
        print("COULDN'T FIND A PRODUCT WITH THAT ID. PLEASE CHECK THE ID.", product)

def create_product():#Create Definition
    print("OK. What is the product's info?")
    product = {"id": auto_incremented_id()}
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
        products.append(product)
        print("CREATING PRODUCT HERE.", product)

def update_product():#Update Definition
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFO...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE.", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH THAT ID. PLEASE CHECK THE ID.", product_id)

def destroy_product():#Destroy Definition
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH THAT ID. PLEASE CHECK THE ID.", product_id)

chosen_operation = input(menu)
liaison(chosen_operation)

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"]) #Writing checkpoint
    writer.writeheader() # uses fieldnames set above
    for product in products:
        writer.writerow(product)
#
#if chosen_operation.title() == "List":
#elif chosen_operation.title() == "Show":

#else:print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")
