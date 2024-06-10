""" defines shorter user choices in coffee dictionary """
coffee_types={'e':'espresso','l': 'latte', 'c': 'cappuccino'}
# print(coffee_types['e'])


def coffee_choice():
    """ interpets the user choice"""
    coffee_type = input("What would you like? 'e' - espresso 'l' - latte 'c' - cappuccino): ")
    coffee = coffee_types[coffee_type]
    return coffee

print(coffee_choice())

def report():
    """prints a report on the coffee resource status"""
    pass


def make_brew():
    """makes the coffee and presents it to the customer"""
    pass


def accept_payment():
    """requests and checks payment value"""
    pass
