"""
The goal is to create the change system of a vending machine
where given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer.
Our function should pay the minimum number of coins possible, and the available coin denominations are 100, 50, 20, 10, 5, 2, and 1.

"""

# Before we start writing our functions, let's import the byotest framework which will be used for test-driven development

from byotest import *

# Create a dictionary with denomination of coin and its quantity as key, value
usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}

def get_change(amount, coins=eur_coins):  # Here if we don't provide the coin type or currency it will default to euro coins
    
    # Unlike a list, looping through a dictionary does not keep the order.
    # Therefore we use `sorted()` to sort the order. This will sstart with the
    # lowest by default, so we use `reverse=True` to start with the highest
    # denomination. The `while` ends when the domination quantity reaches 0.
    # An exception is thrown if there are insufficient coins to give change.
    change = []
    for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins [denomination] > 0:
            amount -= denomination
            coins [denomination] -= 1
            change.append(denomination)
    
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
        
    return change  
        

# In our fist test, we expect an empty list when the actual amount of change equals to zero
test_are_equal(get_change(0),[])

# Our second test will handle the situation where the change equals to a single coin
test_are_equal(get_change(1),[1])

# The thirs test is for a case where cases other than one coin whould be given back to the customer
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])

# The fourth case is the case when we need change in more than one coin as the amount is not a nice, even denomination like 3
test_are_equal(get_change(3),[2,1])

# The fifth case is an even more specific case in order to make our function more general
test_are_equal(get_change(7),[5,2])

# The following test is when we need more than one of a particula denomination of a coin
test_are_equal(get_change(14),[10, 2, 2])

#The last test adds a second argument to the get_change function
test_are_equal(get_change(35, usd_coins),[25, 10])
test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}), "Insufficient coins to give change.")

print("All tests pass!")