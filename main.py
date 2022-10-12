from resources import resources, MENU


def print_report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def is_valid_choice(choice):
    if choice != 'latte' and choice != 'espresso' and choice != 'cappuccino':
        print("Invalid option")
        return False
    else:
        return True


def have_resources(choice):
    if resources['water'] < MENU[choice]['ingredients']['water']:
        print("Sorry there is not enough water")
        return False
    elif resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print("Sorry there is not enough coffee")
        return False
    elif choice != 'espresso':
        if resources['milk'] < MENU[choice]['ingredients']['milk']:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    else:
        return True


def have_coins(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total > MENU[choice]['cost']:
        total -= MENU[choice]['cost']
        total = round(total, 2)
        print(f"Here is ${total} in change.")
        return True
    elif total == MENU[choice]['cost']:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_resource(choice):
    resources['money'] += MENU[choice]['cost']
    resources['water'] -= MENU[choice]['ingredients']['water']
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    if choice != 'espresso':
        resources['milk'] -= MENU[choice]['ingredients']['milk']


user_choice = ""
while user_choice != 'off':
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        print_report()
    elif user_choice == 'off':
        print("Bye")
    else:
        if is_valid_choice(user_choice):
            if have_resources(user_choice):
                if have_coins(user_choice):
                    update_resource(user_choice)
                    print(f"Here is your {user_choice} ☕. Enjoy!")
