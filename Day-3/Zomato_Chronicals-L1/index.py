import json

def load_menu():
    with open('menu.json', 'r') as file:
        menu = json.load(file)
    return menu

def save_menu(menu):
    with open('menu.json', 'w') as file:
        json.dump(menu, file, indent=4)

#--- print the menu data ----------**------
def print_menu():
    with open('menu.json', 'r') as file:
        menu = json.load(file)
        for dish in menu:
            print(f"ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Available: {dish['available']}")

# print_menu()


class MumChronicals:

    @staticmethod
    def add(id, name, price, available):
        menu = load_menu()
        menu.append({"id": id, "name": name, "price": price, "available": available})
        save_menu(menu)

    @staticmethod
    def remove(snack_id):
        menu = load_menu()
        menu = [snack for snack in menu if snack['id'] != snack_id]
        save_menu(menu)

    @staticmethod
    def update_availability(snack_id, new_availability):
        menu = load_menu()
        for snack in menu:
            if snack['id'] == snack_id:
                snack['available'] = new_availability
        save_menu(menu)


# MumChronicals.add(3, 'Pasta', 12, True)
# MumChronicals.remove(4)
# MumChronicals.update_availability(4, False)






def load_orders():
    try:
        with open('orders.json', 'r') as file:
            orders = json.load(file)
    except FileNotFoundError:
        orders = []
    return orders


def save_orders(orders):
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)


def calculate_total_price(order):
    menu = load_menu()
    total_price = sum(dish['price'] for dish in menu if dish['id'] in order['dishIDs'])
    return total_price

def take_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
    dish_ids = [int(id.strip()) for id in dish_ids]

    menu = load_menu()
    available_dish_ids = [dish['id'] for dish in menu if dish['available']]

    if all(dish_id in available_dish_ids for dish_id in dish_ids):
        orders = load_orders()
        order_id = len(orders) + 1
        status = "received"
        new_order = {"id": order_id, "customerName": customer_name, "dishIDs": dish_ids, "status": status}
        orders.append(new_order)
        save_orders(orders)
        print(f"Order {order_id} received successfully.")
        total_price = calculate_total_price(new_order)
        print(f"Total Price: {total_price} INR")
    else:
        print("Error: Some dishes are not available or don't exist.")

def update_order_status():
    order_id = int(input("Enter order ID: "))
    new_status = input("Enter new status: ")

    orders = load_orders()
    order = next((order for order in orders if order["id"] == order_id), None)

    if order:
        order["status"] = new_status
        save_orders(orders)
        print(f"Order {order_id} status updated to {new_status}.")
    else:
        print(f"Error: Order with ID {order_id} not found.")

def review_orders():
    orders = load_orders()
    if orders:
        for order in orders:
            print(f"Order ID: {order['id']}, Customer: {order['customerName']}, Status: {order['status']}")
    else:
        print("No orders available.")

def exit_operations():
    print("Day's operations have been concluded.")

def filter_orders_by_status():
    status = input("Enter the status to filter by: ")
    orders = load_orders()
    filtered_orders = [order for order in orders if order['status'] == status]
    
    if filtered_orders:
        for order in filtered_orders:
            print(f"Order ID: {order['id']}, Customer: {order['customerName']}, Status: {order['status']}")
    else:
        print(f"No orders with status '{status}' found.")



# Calling the respective functions based on user input

# ----------order-operations-----------------

# print_menu()
# take_order()
# update_order_status()
# review_orders()
exit_operations()
# filter_orders_by_status()

# ----------menu-operations-----------------

# MumChronicals.add(5, 'abc', 16, True)
# MumChronicals.remove(5)
# print_menu()
# MumChronicals.update_availability(4, True)
# print_menu()







#--- print the menu data ----------**------
# def print_menu():
#     with open('menu.json', 'r') as file:
#         menu = json.load(file)
#         for dish in menu:
#             print(f"ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Available: {dish['available']}")

# print_menu()


# # -----add data-----------------------**--------
# # menu = load_menu()
# # menu.append({"id": 3, "name": "Pasta", "price": 12, "available": True})
# # save_menu(menu)
# # ------------------------------------**--------


#--- print the menu data ----------**------
def print_orders():
    with open('orders.json', 'r') as file:
        orders = json.load(file)
        for dish in orders:
            print(f"ID: {dish['id']}, Customer_Name: {dish['customerName']}, dishIDs: {dish['dishIDs']}, Status: {dish['status']}")

# print_orders()