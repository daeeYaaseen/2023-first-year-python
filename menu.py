def display_menu():
    print("MENU")
    print("1) Burger")
    print("2) Pizza")
    print("3) Quit")

def display_burger_menu():
    print("1) Chicken R35")
    print("2) Beef R40")
    print("3) Vegan R45")

def display_pizza_menu():
    print("1) Small R25")
    print("2) Medium R50")
    print("3) Large R75")

def display_beverage_menu():
    print("1) Cola R10")
    print("2) Juice R13")
    print("3) Coffee R16")

def calculate_total(order):
    total = 0
    for item in order:
        total += item["price"] * item["quantity"]
    return total

def write_order_to_file(order, total):
    with open("orders.txt", "a") as file:
        file.write("ORDER DETAILS\n")
        for item in order:
            file.write(f"- {item['quantity']} x {item['name']} {item['price']}\n")
        file.write(f"Total = R{total}\n")
        file.write("====================================\n")

def order_food():
    order = []
    total = 0

    display_menu()
    choice = int(input("Please enter your choice: "))

    while choice != 3:
        if choice == 1:
            display_burger_menu()
            flavor_choice = int(input("Please enter your choice (flavor): "))
            if flavor_choice == 1:
                flavor = "Chicken"
                price = 35
            elif flavor_choice == 2:
                flavor = "Beef"
                price = 40
            elif flavor_choice == 3:
                flavor = "Vegan"
                price = 45
            else:
                print("Invalid choice!")
                continue

            quantity = int(input("Please enter quantity: "))
            order.append({"name": f"{flavor} Burger", "price": price, "quantity": quantity})
        elif choice == 2:
            display_pizza_menu()
            size_choice = int(input("Please enter your choice (size): "))
            if size_choice == 1:
                size = "Small"
                price = 25
            elif size_choice == 2:
                size = "Medium"
                price = 50
            elif size_choice == 3:
                size = "Large"
                price = 75
            else:
                print("Invalid choice!")
                continue

            quantity = int(input("Please enter quantity: "))
            order.append({"name": f"{size} Pizza", "price": price, "quantity": quantity})
        else:
            print("Invalid choice!")

        choice = int(input("Please enter your choice: "))

    if len(order) == 0:
        print("No items were ordered. Goodbye!")
        return

    beverage_choice = input("Would you like to order a drink? (yes/no): ")
    if beverage_choice.lower() == "yes":
        display_beverage_menu()
        beverage_choice = int(input("Please enter your choice: "))

        if beverage_choice == 1:
            beverage_name = "Cola"
            beverage_price = 10
        elif beverage_choice == 2:
            beverage_name = "Juice"
            beverage_price = 13
        elif beverage_choice == 3:
            beverage_name = "Coffee"
            beverage_price = 16
        else:
            print("Invalid choice!")
            beverage_name = ""
            beverage_price = 0

def display_menu():
    print("MENU")
    print("1) Burger")
    print("2) Pizza")
    print("3) Quit")

def display_burger_menu():
    print("1) Chicken R35")
    print("2) Beef R40")
    print("3) Vegan R45")

def display_pizza_menu():
    print("1) Small R25")
    print("2) Medium R50")
    print("3) Large R75")

def display_beverage_menu():
    print("1) Cola R10")
    print("2) Juice R13")
    print("3) Coffee R16")

def calculate_total(order):
    total = 0
    for item in order:
        total += item["price"] * item["quantity"]
    return total

def write_order_to_file(order, total):
    with open("orders.txt", "a") as file:
        file.write("ORDER DETAILS\n")
        for item in order:
            file.write(f"- {item['quantity']} x {item['name']} {item['price']}\n")
        file.write(f"Total = R{total}\n")
        file.write("====================================\n")

def order_food():
    order = []
    total = 0

    display_menu()
    choice = int(input("Please enter your choice: "))

    while choice != 3:
        if choice == 1:
            display_burger_menu()
            flavor_choice = int(input("Please enter your choice (flavor): "))
            if flavor_choice == 1:
                flavor = "Chicken"
                price = 35
            elif flavor_choice == 2:
                flavor = "Beef"
                price = 40
            elif flavor_choice == 3:
                flavor = "Vegan"
                price = 45
            else:
                print("Invalid choice!")
                continue

            quantity = int(input("Please enter quantity: "))
            order.append({"name": f"{flavor} Burger", "price": price, "quantity": quantity})
        elif choice == 2:
            display_pizza_menu()
            size_choice = int(input("Please enter your choice (size): "))
            if size_choice == 1:
                size = "Small"
                price = 25
            elif size_choice == 2:
                size = "Medium"
                price = 50
            elif size_choice == 3:
                size = "Large"
                price = 75
            else:
                print("Invalid choice!")
                continue

            quantity = int(input("Please enter quantity: "))
            order.append({"name": f"{size} Pizza", "price": price, "quantity": quantity})
        else:
            print("Invalid choice!")

        choice = int(input("Please enter your choice: "))

    if len(order) == 0:
        print("No items were ordered. Goodbye!")
        return

    beverage_choice = input("Would you like to order a drink? (yes/no): ")
    if beverage_choice.lower() == "yes":
        display_beverage_menu()
        beverage_choice = int(input("Please enter your choice: "))

        if beverage_choice == 1:
            beverage_name = "Cola"
            beverage_price = 10
        elif beverage_choice == 2:
            beverage_name = "Juice"
            beverage_price = 13
        elif beverage_choice == 3:
            beverage_name = "Coffee"
            beverage_price = 16
        else:
            print("Invalid choice!")
            beverage_name = ""
            beverage_price = 0

