coffeeChoice = ''
resources = {
        "water": 1000.0,  # ml
        "milk": 1000.0,  # ml
        "coffee": 1000.0,  # grams
        "Money": 0.0
    }
while coffeeChoice != "off":
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino): ")

    recipes = {
        # water, milk, coffee, price
        "espresso": [50.0, 0.0, 18.0, 1.50],
        "latte": [200.0, 150.0, 24.0, 2.50],
        "cappuccino": [250.0, 100.0, 24.0, 3.00]
    }

    def get_change(price):
        coins = {
            "quarters": 0.25,
            "dimes": 0.10,
            "nickles": 0.05,
            "pennies": 0.01
        }

        def calc_change(coin_value, coinAmount):

            total_amount = coin_value * float(coinAmount)
            return total_amount

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
        if price > total:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        if total > price:
            total_change = total - price
            print(f"Here is $%.2f in change." % total_change)
            return total_change
        else:
            return 1

    def check_resources(resource, request):
        i = 0
        for key in resource:
            if resource[key] <= request[i]:
                print(f"Sorry there is not enough {key}.")
            resource[key] = resources[key]-request[i]
            i += 1
            if i == 3:
                return resource
        # if request[key][0] > resource[key]:

    if coffeeChoice == "report":
        print('Water: ' + str(int(resources["water"])) + 'ml')
        print('Milk: ' + str(int(resources["milk"])) + 'ml')
        print('Coffee: ' + str(int(resources["coffee"])) + 'g')
        print('Money: $' + str(resources["Money"]))
    elif coffeeChoice == "espresso":
        change = get_change(recipes["espresso"][3])
        if change != 0:
            resources = check_resources(resources, recipes["espresso"])
            resources["Money"] = resources["Money"] + recipes["espresso"][3]
            print("Here is your espresso ☕ Enjoy!")
    elif coffeeChoice == "latte":
        change = get_change(recipes["latte"][3])
        if change != 0:
            resources = check_resources(resources, recipes["latte"])
            resources["Money"] = resources["Money"] + recipes["latte"][3]
            print("Here is your latte ☕ Enjoy!")
    elif coffeeChoice == "cappuccino":
        change = get_change(recipes["cappuccino"][3])
        if change != 0:
            resources = check_resources(resources, recipes["cappuccino"])
            resources["Money"] = resources["Money"] + recipes["cappuccino"][3]
            print("Here is your cappuccino ☕ Enjoy!")
    else:
        print("Enter the available choices: espresso / latte / cappuccino / report / off")
