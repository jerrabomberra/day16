coffee_types={'e':'espresso','l': 'latte', 'c': 'cappuccino'}
# print(coffee_types['e'])


def coffee_choice():
    coffee_type = input("What would you like? ('e' for espresso 'l' for latte 'c' for cappuccino)? : ")
    coffee = coffee_types[coffee_type]
    return coffee

print(coffee_choice())
