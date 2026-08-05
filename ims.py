inventory=[

{"id": 101, "name": "M3 Pro MacBook", "category": "Electronics", "price": 1999.99, "stock": 12, "rating": 4.8},

{"id": 102, "name": "MX Master 3S Mouse", "category": "Electronics", "price": 99.99, "stock": 45, "rating": 4.7},

{"id": 103, "name": "Ergonomic Desk Chair", "category": "Furniture", "price": 349.50, "stock": 8, "rating": 4.3},

{"id": 104, "name": "34\" UltraWide Monitor", "category":

"Electronics", "price": 699.00, "stock": 0, "rating": 4.6}, {"id": 105, "name": "Keychron Keyboard", "category": "Electronics",

"price": 129.99, "stock": 25, "rating": 4.5}

]


def add_to_store():
    global inventory
    id = int(input("enter product id"))
    name=input("Enter product name: ")
    category=input("Enter product category: ")
    price=input("Enter product price: ")
    stock=input("Enter product stock: ")
    rating=input("Enter product rating: ")


    new_product = {
        "id": id,
        "name": name,
        "category":category,
        "price":price,
        "stock":stock,
        "rating":rating,


    }

    inventory.append(new_product)


# add_to_store()

def view_product(inventory):
    print("="*15,"current store catalog","="*15)
    print (f"id" "\t",      "product_name","\t",       "category","\t",       "price","\t","stock")
    #print(f"{id":<6}  {,product_name':<25}  {'category':<15 } { 'price':<12}  {'stock':<8}")

    print("-"* 50)
    for product in inventory:
        print(f"{product['id']:<6}     {product['name']:<25}  {product['category']:<15}  {product['price']:<12}  {product['stock']:<8}")


#view_product(inventory)

def delete_product(inventory):
    id = int(input("enter product id"))

    def delete_by_id( list):
        return list["id"] != id

    new_inventory = list(filter(delete_by_id, inventory))
    return new_inventory




# inventory=delete_product(inventory)
# view_product(inventory)


def search_by_category(inventory):
    category = input("Enter category: ")

    def search_category(product):
        return product["category"] == category

    result = list(filter(search_category, inventory))
    view_product(list(result))
#search_results=search_by_category(inventory)



def search_by_name(inventory):
    name=input("Enter product name: ")
    def search_by_name(product):
        return product["name"].lower() == name.lower()
    result = list(filter(search_by_name, inventory))

    view_product(list(result))
#search_results=search_by_name(inventory)


def update_stock(inventory):
    id = int(input("enter product id"))
    stock=input("Enter product stock: ")
    def update_stock_by_id(product):
        if(product["id"]==id):
            product["stock"] = stock
        return product
    result = list(map(update_stock_by_id, inventory))
    
    view_product(list(result))


#update_stock(inventory)
def view_in_stocks(inventory):
    def in_stocks(product):
        return product["stock"]>0

    result=list(filter(in_stocks, inventory))
    view_product(result)





def main ():
    print ("welcome to Inventory Management System")
    while True:
        print("Please Enter 1 for adding Product")
        print("Please Enter 2 for viewing Products")
        print("Please Enter 3 for search by name")
        print("Please Enter 4 for search by category")
        print("Please Enter 5 for update stock")
        print("please Enter 6 for view in stocks product")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_to_store()
        elif choice == 2:
                view_product(inventory)
        elif choice == 3:
                search_by_name(inventory)
        elif choice == 4:
                search_by_category(inventory)
        elif choice == 5:
                update_stock(inventory)
        elif choice == 6:
                view_in_stocks(inventory)
        else:
                print("good bye")
main()