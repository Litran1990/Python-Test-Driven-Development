# In this module we will be buidling our own test framework that we can use with our own functions.

# A way to make our tests more robust is to include our assertions into a function so we will be able to see the actual values and not only the error.
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_is_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)
    
def test_is_in_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)
    

#Calling the functions in order to test the assertions

# test_not_equal(0, 0)

# test_is_in([1, 2, 3, 4, 5], 7)