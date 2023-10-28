# Define a class named 'Snack' to represent individual snacks.
class Snack:
    # Constructor method. It initializes the attributes of the snack.
    def __init__(self, id, name, price, availability):
        # Assign the provided values to the attributes of the snack.
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability

# Sample Usage
# Create an instance of the 'Snack' class with specific attributes.
snack1 = Snack(1, "Chocolate Chip Cookies", 1.5, "yes")
# Create another instance of the 'Snack' class with different attributes.
snack2 = Snack(2, "Potato Chips", 1.0, "yes")

# print(snack1.name)

# ------------------------------------------------------------------------------

# Define a class named 'SnackInventory' to manage the list of snacks.
class SnackInventory:
    # Constructor method. Initialize an empty list to store snacks.
    def __init__(self):
        self.snacks = []

    #1- Method to add a snack to the inventory.
    def add_snack(self, snack):
        # Append the provided snack to the list of snacks.
        self.snacks.append(snack)

    #2- Method to remove a snack from the inventory based on its ID.
    def remove_snack(self, snack_id):
        # Use a list comprehension to filter out the snack with the specified ID.
        self.snacks = [snack for snack in self.snacks if snack.id != snack_id]

    #3- Method to update the availability of a snack based on its ID.
    def update_availability(self, snack_id, new_availability):
        # Iterate through the list of snacks.
        for snack in self.snacks:
            # If the snack has the specified ID, update its availability.
            if snack.id == snack_id:
                snack.availability = new_availability


     #4- Method to handle the sale of a snack. with proper error handling
    def sell_snack(self, snack_id):
        if not isinstance(snack_id, int) or snack_id <= 0:
            print("Invalid input. Please enter a positive integer as snack ID.")
            return

        for snack in self.snacks:
            if snack.id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    self.record_sale(snack)
                    print(f"Snack '{snack.name}' sold successfully!")
                else:
                    print(f"Snack '{snack.name}' is not available.")
                return

        print(f"No snack found with ID {snack_id}.")

    #5- Method to record the sale of a snack. it will generate a file for the sold snacks
    def record_sale(self, snack):
        with open("sales_records.txt", "a") as file:
            file.write(f"Snack ID: {snack.id}, Name: {snack.name}, Price: {snack.price}\n")
    
   
    

    def display_snacks(self):
        for snack in self.snacks:
            print(f"ID: {snack.id}, Name: {snack.name}, Price: ${snack.price}, Availability: {snack.availability}")

# specifically for level 2


    def display_menu(self):
        print("Welcome to Mumbai Munchies Canteen!")
        print("1. Display Snacks Inventory")
        print("2. Sell Snack")
        print("3. Add Snack")
        print("4. Remove Snack")
        print("5. Update Availability")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.display_snacks()
            elif choice == '2':
                snack_id = int(input("Enter the ID of the snack you want to sell: "))
                self.sell_snack(snack_id)
            elif choice == '3':
                id = int(input("Enter ID for the new snack: "))
                name = input("Enter name for the new snack: ")
                price = float(input("Enter price for the new snack: "))
                availability = input("Enter availability for the new snack (yes/no): ")
                new_snack = Snack(id, name, price, availability)
                self.add_snack(new_snack)
            elif choice == '4':
                snack_id = int(input("Enter the ID of the snack you want to remove: "))
                self.remove_snack(snack_id)
            elif choice == '5':
                snack_id = int(input("Enter the ID of the snack you want to update: "))
                new_availability = input("Enter new availability for the snack (yes/no): ")
                self.update_availability(snack_id, new_availability)
            elif choice == '6':
                print("Thank you for using Mumbai Munchies Canteen System!")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")

# Sample Usage
# Create an instance of the 'SnackInventory' class.
inventory = SnackInventory()
# Create a new snack using the 'Snack' class.
snack3 = Snack(3, "Granola Bars", 2.0, "yes")
# Add the new snack to the inventory.
inventory.add_snack(snack1)
inventory.add_snack(snack2)
inventory.add_snack(snack3)

# Removing a snack with ID 2 from the inventory.
# inventory.remove_snack(2)

# Updating the availability of a snack with ID 1 to 'no'.
# inventory.update_availability(1, "no")

# Display the current status of all snacks in the inventory.
# inventory.display_snacks()
# inventory.sell_snack(3)
# inventory.display_snacks()






# -------------------------------------------------------------------lv 2

# Sample Usage
inventory = SnackInventory()
inventory.run()
