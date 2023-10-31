import json

def load_menu():
    with open('menu.json', 'r') as file:
        menu = json.load(file)
    return menu

def save_menu(menu):
    with open('menu.json', 'w') as file:
        json.dump(menu, file, indent=4)

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

























#--- print the menu data ----------**------
def print_menu():
    with open('menu.json', 'r') as file:
        menu = json.load(file)
        for dish in menu:
            print(f"ID: {dish['id']}, Name: {dish['name']}, Price: {dish['price']}, Available: {dish['available']}")

print_menu()


# # -----add data-----------------------**--------
# # menu = load_menu()
# # menu.append({"id": 3, "name": "Pasta", "price": 12, "available": True})
# # save_menu(menu)
# # ------------------------------------**--------