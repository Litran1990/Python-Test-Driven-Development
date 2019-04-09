# In this case we will be testing our functions while writing our code as we build the functions incrementally

def even_number_of_evens(numbers):
    if numbers == []:
        return False
    
    # By inserting this line we have assert number 2 returning True...
    # Basically we have to look for tests which will cause our program to fail!
    # else:
    #     return True
    
    # In order to solve the third assert we commented out the line above and replaced by the one below...
    evens = 0
    
    # plus, we inserted a for loop in order to get a False in assert 3
    for n in numbers:
        if n % 2 == 0:
            evens += 1
            
    # For assert 4 we need to add a function in case evens equals to 0
    if evens == 0:
        return False
    else:    
        return evens % 2 == 0
    

# The first assert is simply looking for a False outcome
assert even_number_of_evens([]) == False, "No numbers"

# As we are building our fucntion incrementally, we should look for a next assert which should equal to True, therefore resulting in an error.
# Once the error is confirmed, we can then build the function.
assert even_number_of_evens([2, 4]) == True, "Two even numbers"

# The third assert is looking for a False as we have only one even number
assert even_number_of_evens([2]) == False, "Only one even number"

# The fourth assert is when we have an odd number of odd numbers
assert even_number_of_evens([1, 3, 9]) == False, "Three odd numbers"

print("All tests passed!")