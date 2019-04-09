# Here we will write our tests after the function has been written

# Version 1
def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
# Using the assertion method we can now test the function above
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("**$£") == 0, "Special characters"

# In case the value inserted by the end-user passes all the tests above, a message will be printed
print("All the tests passed")


#Version 2

# Testing a new version of the function
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
# Using the assertion method we can now test the function above
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("AA") == 2, "Two upper case"
assert count_upper_case("a") == 0, "One lower case"  
assert count_upper_case("**$£") == 0, "Special characters"

# In case the value inserted by the end-user passes all the tests above, a message will be printed
print("All the tests passed")