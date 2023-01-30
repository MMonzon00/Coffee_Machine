coffeeChoice = ''
while coffeeChoice != "off":
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino): ")

    resources = {
        "water": 1000.0,  # ml
        "milk": 1000.0,  # ml
        "coffee": 1000.0,  # grams
        "Money": 0.0
    }
    recipes = {
        # water, milk, coffee, price
        "espresso": [50.0, 0, 18, 1.50],
        "latte": [200.0, 150.0, 24, 2.50],
        "cappuccino": [250, 100, 24, 3.00]
    }

    def get_change(price):
        coins = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01
        }

        def calc_change(coin_value, coin_amount):

            total = coin_value * float(coin_amount)
            return total

        total = 0

        print("Please insert coins.")
        coin_amount = (input("How many quarters?: "))
        amount = calc_change(coins["quarters"], coin_amount)
        total = total + amount
        coin_amount = (input("How many dimes?: "))
        amount = calc_change(coins["dimes"], coin_amount)
        total = total + amount
        coin_amount = (input("How many nickles?: "))
        amount = calc_change(coins["nickles"], coin_amount)
        total = total + amount
        coin_amount = (input("How many pennies?: "))
        amount = calc_change(coins["pennies"], coin_amount)
        total = total + amount
        print(total)
        print(price)
        if price > total:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        else:
            change = total-price
            print(f"Here is $%.2f in change." % change)
            return change

    def check_resources(resource, request):
        i = 0
        for key in resource:
            if resource[key] < request[i]:
                print(f"Sorry there is not enough {key}.")
            resource[key] = resources[key]-request[i]
            i += 1
            if i == 3:
                return resource
        # if request[key][0] > resource[key]:

    if coffeeChoice == "report":
        print('water: ' + str(int(resources["water"])) + 'ml')
        print('milk: ' + str(int(resources["milk"])) + 'ml')
        print('coffee: ' + str(int(resources["coffee"])) + 'g')
        print('Money: $' + str(resources["Money"]))
    elif coffeeChoice == "espresso":
        change = get_change(recipes["espresso"][3])
        if change != 0:
            resources = check_resources(resources, recipes["espresso"])
            resources["Money"] = resources["Money"] + recipes["espresso"][3]
    elif coffeeChoice == "latte":
        change = get_change(recipes["latte"][3])
        if change != 0:
            resources = check_resources(resources, recipes["latte"])
            resources["Money"] = resources["Money"] + recipes["latte"][3]
    elif coffeeChoice == "cappuccino":
        change = get_change(recipes["cappuccino"][3])
        if change != 0:
            resources = check_resources(resources, recipes["cappuccino"])
            resources["Money"] = resources["Money"] + recipes["cappuccino"][3]
    else:
        print("Enter the available choices: espresso / latte / cappuccino / report / off")