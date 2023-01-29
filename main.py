coffeeChoice = ''
while coffeeChoice != "off":
    coffeeChoice = input("What would you like? (espresso/latte/cappuccino): ")
    total
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    resources = {
        "water": 1000.0,  # ml
        "milk": 1000.0,  # ml
        "coffee": 1000.0,  # grams
        "Money": 0.0
    }
    recipes = {
        # water, milk, coffee, price
        "espresso": [1001.0, 0, 18, 1.50],
        "latte": [200.0, 150.0, 24, 2.50],
        "cappuccino": [250, 100, 24, 3.00]
    }

    def calc_change(coin_total):
        change = 0
        for i in coin_total:
            change += coin_total[i]
        return change

    def check_resources(resource, request):
        i = 0
        for key in resource:
            if resource[key] < request[i]:
                print(f"Sorry there is not enough {key}.")
            i += 1
            if i == 3:
                break;
        # if request[key][0] > resource[key]:
    
    if coffeeChoice == "report":
        print('water: ' + str(int(resources["water"])) + 'ml')
        print('milk: ' + str(int(resources["milk"])) + 'ml')
        print('coffee: ' + str(int(resources["coffee"])) + 'g')
        print('Money: $' + str(resources["Money"]))
    elif coffeeChoice == "espresso":

        check_resources(resources, recipes["espresso"])
    elif coffeeChoice == "latte":
        check_resources(resources, recipes["latte"])
    elif coffeeChoice == "cappuccino":
    check_resources(resources, recipes["cappuccino"])
