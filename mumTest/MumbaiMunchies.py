import json
import random
import datetime


role = 0
inven = open("./Inventory.json", "r")
salesFile = open("./Sales.json", "r")
securityFile = open("./security.json", "r")
inventory = eval(inven.read())
sales = eval(salesFile.read())
security = eval(securityFile.read())

def findInput(msg, options):
    inp = input(msg)
    if(inp in options):
        return inp
    else:
        print("Please choose correct option!")
        findInput(msg, options)

def exit(val):
    global inventory
    global sales
    global security
    updateInven = open("./Inventory.json", "w")
    updateInven.write(json.dumps(inventory))
    updateSales = open("./Sales.json", "w")
    updateSales.write(json.dumps(sales))
    updateSecurity = open("./security.json", "w")
    updateSecurity.write(json.dumps(security))
    print(f"good Bye {val}...")

def generateDigit():
    return random.randint(1000, 9999)

def showItems(dicts):
    for item in dicts:
        print(f"{dicts.get(item)}")

def addNewItem():
    newId = input("New Item ID:")
    name = input("Item Name:")
    price = int(input("Snack Price:"))
    available = findInput("Snack Available(Yes or No):", ['Yes', 'No'])

    obj = {"id": newId, "name": name, "price" :price, "available": available }
    return obj

def updateItem(id):
    name = input("Updated Name:")
    price = int(input("Updated Price:"))
    available = findInput("Item Available(Yes or No):", ['Yes', 'No'])

    obj = {"id": id, "name": name, "price" :price, "available": available }
    return obj

def getOrderItems():
    single = ""
    order = []
    while(single != "c"):
        try:
            single = input("item name (c for completed):")
            if(single == 'c'):
                break
            quantity = int(input("item quantity:"))
            order.append({single: quantity})
        except:
            print("please enter correct value")
    return order

def addNewSale(key):
    try:
        billId = generateDigit()
        while billId in key:
            billId = generateDigit()
        itemList = getOrderItems()
        bill = int(input("Total Bill Amount:"))
        today = datetime.date.today()
        date = today.strftime("%d/%m/%Y")
        payment = findInput("Payment Mode(cash, upi):", ['cash', 'upi'])

        obj = { "billId": str(billId),"items with quantity": itemList, "date": date, "payment": payment, "bill": bill}
        return obj
    except:
        print("please enter correct details")
        addNewSale()

def updateSale(id):
    try:
        itemList = getOrderItems()
        bill = int(input("Total Bill Amount:"))
        today = datetime.date.today()
        date = today.strftime("%d/%m/%Y")
        payment = findInput("Payment Mode(cash, upi):", ['cash', 'upi'])

        obj = { "billId": str(id),"items with quantity": itemList, "date": date, "payment": payment, "bill": bill}
        return obj
    except:
        print("please enter correct details")
        updateSale(id)


def adminRole():
    print("\n---------Mumbai Munchies------------")
    print("|        1. Inventory              |")
    print("|        2. Sales                  |")
    print("|        3. Security               |")
    print("|        4. Main Menu              |")
    print("|        5. Exit                   |")
    print("------------------------------------")
    try:
        option = int(input("Choose one option:"))
        if(option > 5 or option <= 0):
            print("Please choose correct option")
            adminRole()
        else:
            global inventory
            global sales
            global security
            if(option == 1):
                print("\n---------Mumbai Munchies----------")
                print("|        1. View Inventory        |")
                print("|        2. Add new Item          |")
                print("|        3. Update Item           |")
                print("|        4. Delete Item           |")
                print("|        5. Main Menu             |")
                print("|        6. Exit                  |")
                print("----------------------------------")
                try:
                    InventoryOption = int(input("Choose one option:"))
                    if(InventoryOption > 6 or InventoryOption <= 0):
                        print("Please choose correct option")
                        adminRole()
                    elif(InventoryOption == 1):
                        showItems(inventory)
                        adminRole()
                    elif(InventoryOption == 2):
                        obj = addNewItem()
                        inventory.update({ obj["id"]:  obj})
                        print("Item has added")
                        adminRole()
                    elif(InventoryOption == 3):
                        updateId = findInput("Item ID:", list(inventory.keys()))
                        obj = updateItem(updateId)
                        print(obj)
                        inventory.update({str(updateId) : obj})
                        adminRole()
                    elif(InventoryOption == 4):
                        deleteId = findInput("Item ID:", list(inventory.keys()))
                        inventory.pop(deleteId)
                        print("Item has been deleted")
                        adminRole()
                    elif(InventoryOption == 5):
                        adminRole()
                    elif(InventoryOption == 6):
                        exit("Admin")
                except:
                    print("\nPlease enter correct option")
                    adminRole()
            elif(option == 2):
                print("\n---------Mumbai Munchies----------")
                print("|        1. View Sales            |")
                print("|        2. Add new bill          |")
                print("|        3. Update bill           |")
                print("|        4. Delete bill           |")
                print("|        5. Main Menu             |")
                print("|        6. Exit                  |")
                print("-----------------------------------")
                try:
                    SaleOption = int(input("Choose one option:"))
                    if(SaleOption > 6 or SaleOption <= 0):
                        print("Please choose correct option")
                        adminRole()
                    elif(SaleOption == 1):
                        showItems(sales)
                        adminRole()
                    elif(SaleOption == 2):
                        obj = addNewSale(list(sales.keys()))
                        print(obj)
                        sales.update({obj["billId"]: obj})
                        adminRole()
                    elif(SaleOption == 3):
                        updateId = findInput("Bill ID:", list(sales.keys()))
                        obj = updateSale(updateId)
                        print(obj)
                        sales.update({updateId: obj})
                        pass
                    elif(SaleOption == 4):
                        deleteId = findInput("Bill ID:", list(sales.keys()))
                        sales.pop(deleteId)
                        print("Bill has been deleted")
                        adminRole()
                    elif(SaleOption == 5):
                        adminRole()
                    elif(SaleOption == 6):
                        exit("Admin")
                except:
                    print("\nPlease enter correct option")
                    adminRole()
            elif(option == 3):
                print("\n---------Mumbai Munchies----------")
                print("|        1. View Passwords        |")
                print("|        2. Add/Update Password   |")
                print("|        3. Delete Password       |")
                print("|        4. Main Menu             |")
                print("|        5. Exit                  |")
                print("----------------------------------")
                try:
                    PassOption = int(input("Choose one option:"))
                    if(PassOption > 5 or PassOption <= 0):
                        print("Please choose correct option")
                        adminRole()
                    elif(PassOption == 1):
                        print(security)
                        adminRole()
                    elif(PassOption == 2):
                        newRole = input("Role:")
                        newPass = input("Password:")
                        security.update({newRole: newPass})
                        adminRole()
                    elif(PassOption == 3):
                        deleteRole = input("Role:")
                        security.pop(deleteRole)
                        adminRole()
                    elif(PassOption == 4):
                        adminRole()
                    elif(PassOption == 5):
                        exit("Admin")
                except:
                    print("please choose correct option")
                    adminRole()
            elif(option == 4):
                defineRole()
            elif(option == 5):
                exit("Admin")
    except:
        print("\nPlease enter correct option")
        adminRole()


def staffRole():
    print("\n---------Mumbai Munchies----------")
    print("|        1. View Snack           |")
    print("|        2. Add Snack            |")
    print("|        3. Remove Snack         |")
    print("|        4. Update Availability  |")
    print("|        5. Main Menu            |")
    print("|        6. Exit                 |")
    print("----------------------------------")
    try:
        option = int(input("Choose one option:"))
        if(option > 6 or option <= 0):
            print("Please choose correct option")
            staffRole()
        else:
            global inventory
            if(option == 1):
                showItems(inventory)
                staffRole()
            elif(option == 2):
                obj = addNewItem()
                inventory.update({ obj["id"]:  obj})
                print("Item has added")
                staffRole()
                
            elif(option == 3):
                remove = input("Snack ID:")
                inventory.pop(remove)
                print("Item has removed sccuessfully.")
                staffRole()
            elif(option == 4):
                updateId = findInput("Snack ID:", list(inventory.keys()))
                avail = findInput("Snack is Available? (Yes or No):", ['Yes', 'No'])
                inventory.update({updateId: {
                        **inventory[updateId],
                        "available": avail}})
                    
                print("Item has updated:", inventory[updateId])
                staffRole()
            elif(option == 5):
                defineRole() 
            elif(option == 6):
                exit("Staff")
            
    except:
        print("\nPlease enter correct option")
        staffRole()

def cashierRole():
    print("\n---------Mumbai Munchies----------")
    print("|        1. View Bills           |")
    print("|        2. Create Bill          |")
    print("|        3. Main Menu            |")
    print("|        4. Exit                 |")
    print("----------------------------------")
    try:
        option = int(input("Choose one option:"))
        if(option > 4 or option <= 0):
            print("Please choose correct option")
            cashierRole()
        else:
            global sales
            if(option == 1):
                showItems(sales)
                cashierRole()
            elif(option == 2):
                obj = addNewSale(list(sales.keys()))
                print(obj)
                sales.update({obj["billId"] : obj})
                cashierRole()
            elif(option == 3):
                defineRole() 
            elif(option == 4):
                exit("Cashier")
    except:
        print("please enter correct options")
        cashierRole()


def defineRole():
    global role
    print("\n-----Mumbai Munchies------")
    print("|        1. Admin        |")
    print("|        2. Staff        |")
    print("|        3. Cashier      |")
    print("|        4. Exit         |")
    print("--------------------------")
    try:
        role = int(input("Choose one role:"))
        if(role > 4 or role <= 0):
            print("Please choose correct role")
            defineRole()
        else:
            global security
            
            
            if(role == 1):
                password = input("Enter Password:")
                if(security["admin"] == password):
                    adminRole()
                else:
                    print("wrong password. try again....")
                    defineRole()
            elif(role == 2):
                password = input("Enter Password:")
                if(security["staff"] == password):
                    staffRole()
                else:
                    print("wrong password. try again....")
                    defineRole()
            elif(role == 3):
                password = input("Enter Password:")
                if(security["cashier"] == password):
                    cashierRole()
                else:
                    print("wrong password. try again....")
                    defineRole()
            elif(role == 4):
                print("Good Bye...")
    except:
        print("\nPlease choose correct role")
        defineRole()

defineRole()