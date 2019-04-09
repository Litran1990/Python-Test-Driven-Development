# Here we will first wirte our tests and then define our function

# In the first assert we must make sure that when numbers equals to none the outcome it "No numbers"
def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0
        
# For the second assert, we must increment the var evens by one if the "number" is divisable by 2 or in this case even    
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
    else:
        return evens % 2 == 0


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")