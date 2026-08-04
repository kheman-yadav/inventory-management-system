inventory=[

{"id": 101, "name": "M3 Pro MacBook", "category": "Electronics", "price": 1999.99, "stock": 12, "rating": 4.8},

{"id": 102, "name": "MX Master 3S Mouse", "category": "Electronics", "price": 99.99, "stock": 45, "rating": 4.7},

{"id": 103, "name": "Ergonomic Desk Chair", "category": "Furniture", "price": 349.50, "stock": 8, "rating": 4.3},

{"id": 104, "name": "34\" UltraWide Monitor", "category":

"Electronics", "price": 699.00, "stock": 0, "rating": 4.6}, {"id": 105, "name": "Keychron Keyboard", "category": "Electronics",

"price": 129.99, "stock": 25, "rating": 4.5}

]


def add_to_store(num,value):
    return(num.append(value))

def view_store():
    print("="*15,"CURRENT STORE CATALOG","="*15)
    print(f"{["id"]},"/t",{["product_name"]},"/t",{["catagory"]},{["price"]},{"stock"},{["ratings"]}")
    for product in inventory:
        print(f"{product["id"]}\t{product["name"]}\t{product["category"]}\t{product["price"]}\t{product["stock"]}")
              

def delete_from_id():
    id = int(input("Enter the id here: "))

    global inventory
    def delete_by_id(inventoryItem):
        return inventoryItem["id"] != id

    result = list(filter(delete_by_id, inventory))
    inventory = result

delete_from_id()