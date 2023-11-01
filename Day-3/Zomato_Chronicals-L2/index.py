import json
from datetime import datetime

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

from datetime import datetime

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
        
        # Add date and time of the order
        order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_order = {"id": order_id, "customerName": customer_name, "dishIDs": dish_ids, "status": status, "orderTime": order_time}
        
        # Ask for coupon code
        coupon_code = input("Do you have a coupon code? (Enter 'zomato10' for 10% discount, or leave blank): ")
        if coupon_code == 'zomato10':
            total_price = calculate_total_price(new_order) * 0.9  # Apply 10% discount
            print("10% discount applied!")
        else:
            total_price = calculate_total_price(new_order)
        new_order["total_price"]=total_price
        orders.append(new_order)
        save_orders(orders)
        
        print(f"Order {order_id} received successfully.")
        print(f"Order Time: {order_time}")
        print(f"Total Price: {total_price} USD")
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

# -----------filter--------------------------------

def filter_orders_by_status():
    status = input("Enter the status to filter by: ")
    orders = load_orders()
    filtered_orders = [order for order in orders if order['status'] == status]
    
    if filtered_orders:
        for order in filtered_orders:
            print(f"Order ID: {order['id']}, Customer: {order['customerName']}, Status: {order['status']}")
    else:
        print(f"No orders with status '{status}' found.")


# ----------lv2-------------------------


def add_feedback(dish_id, rating, comment):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        if 'feedback' not in dish:
            dish['feedback'] = []
        dish['feedback'].append({'rating': rating, 'comment': comment})
        save_menu(menu)
        print(f"Feedback added for dish ID {dish_id}.")
    else:
        print(f"Error: Dish with ID {dish_id} not found.")

# --------------discount--------------

def apply_discount(dish_id, discount_percentage):
    menu = load_menu()
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        dish['price'] *= (1 - discount_percentage / 100)
        save_menu(menu)
        print(f"Discount applied to dish ID {dish_id}.")
    else:
        print(f"Error: Dish with ID {dish_id} not found.")


# ----------daily-sales---------------
def generate_daily_sales_summary(date):
    orders = load_orders()
    total_sales = 0
    
    for order in orders:
        order_date = datetime.strptime(order["orderTime"], "%Y-%m-%d %H:%M:%S").date()
        
        if order_date == date:
            total_sales += order["total_price"]
    
    return total_sales

# -----------find the most order dish---------------

# def find_most_ordered_dish(date=None):
#     orders = load_orders()
#     dish_frequency = {}
    
#     for order in orders:
#         if date is None or datetime.strptime(order["orderTime"], "%Y-%m-%d %H:%M:%S").date() == date:
#             for dish_id in order["dishIDs"]:
#                 if dish_id in dish_frequency:
#                     dish_frequency[dish_id] += 1
#                 else:
#                     dish_frequency[dish_id] = 1
    
#     if not dish_frequency:
#         return None
    
#     most_ordered_dish_id = max(dish_frequency, key=dish_frequency.get)
#     menu = load_menu()
#     most_ordered_dish = next((dish for dish in menu if dish["id"] == most_ordered_dish_id), None)
    
#     return most_ordered_dish


# To get the order history for a specific customer

def get_customer_order_history():
    customer_name = input("Enter customer name: ")
    orders = load_orders()
    customer_orders = [order for order in orders if order["customerName"] == customer_name]
    order_history =customer_orders
    if order_history:
      for order in order_history:
        print(f"Order ID: {order['id']}, Status: {order['status']}, Total Price: {order['total_price']} USD")
    else:
        print(f"No orders found for customer   {customer_name}.")





def find_most_ordered_dish(date=None):
    orders = load_orders()
    dish_frequency = {}
    
    for order in orders:
        if date is None or datetime.strptime(order["orderTime"], "%Y-%m-%d %H:%M:%S").date() == date:
            for dish_id in order["dishIDs"]:
                if dish_id in dish_frequency:
                    dish_frequency[dish_id] += 1
                else:
                    dish_frequency[dish_id] = 1
    
    if not dish_frequency:
        return None
    
    most_ordered_dish_id = max(dish_frequency, key=dish_frequency.get)
    menu = load_menu()
    most_ordered_dish = next((dish for dish in menu if dish["id"] == most_ordered_dish_id), None)
    
    return most_ordered_dish

def run_most_ordered_dish_report(option):
    if option == "today":
        date = datetime.now().date()
        most_ordered_dish = find_most_ordered_dish(date)
        if most_ordered_dish:
            print(f"The most ordered dish today is: {most_ordered_dish['name']}")
        else:
            print("No orders today.")
    elif option == "overall":
        most_ordered_dish = find_most_ordered_dish()
        if most_ordered_dish:
            print(f"The most ordered dish overall is: {most_ordered_dish['name']}")
        else:
            print("No orders overall.")
    else:
        print("Invalid option. Please use 'today' or 'overall'.")








# Calling the respective functions based on user input

# ----------order-operations-----------------

# print_menu()
# take_order()
# update_order_status()
# review_orders()
# exit_operations()
# filter_orders_by_status()

# ----------menu-operations-----------------

# MumChronicals.add(5, 'abc', 16, True)
# MumChronicals.remove(5)
# print_menu()
# MumChronicals.update_availability(4, True)
# print_menu()

#----------------lv2---------------------------------

# add_feedback(2, 4.4, "nice")
## apply_discount(1, 10)

# ------------*****-------------
# date = datetime.strptime("2023-11-02", "%Y-%m-%d").date()
# sales = generate_daily_sales_summary(date)
# print(f"Total sales on {date}: {sales} USD")


# ------------*****-------------
# To get the order history for a specific customer
# get_customer_order_history()

# ------------*****-------------

# To find the most ordered dish for today
# option = input("Enter 'today' or 'overall': ").strip().lower()
# run_most_ordered_dish_report(option)


















#--- print the menu data ----------**------
# def print_menu():
#     with open('menu.json', 'r') as file:
#         menu = json.load(file)
#         for dish in menu:
#             print(f"ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Available: {dish['available']}")

# print_menu()




#--- print the orders data ----------**------
# def print_orders():
#     with open('orders.json', 'r') as file:
#         orders = json.load(file)
#         for dish in orders:
#             print(f"ID: {dish['id']}, Customer_Name: {dish['customerName']}, dishIDs: {dish['dishIDs']}, Status: {dish['status']}")

# print_orders()