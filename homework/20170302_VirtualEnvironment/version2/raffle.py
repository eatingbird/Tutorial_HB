from random import choice
from customers import *

"""Randomly pick customer and print customer info"""

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    print "Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    return pick_winner(customers)

run_raffle()

# Hint: remember to import any functions you need from
# other files or libraries
