# As our tests in "evens-testing-while.py" have all successfully passed, now we can refactor our code

# Second actions is to check if we are repeting ourselves in order to check if the number is even, thus including the helper below is a way to do so.
def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    
    # First action is to remove the section below as it can be considered repetitive, "evens = 0" is already doing its job
    # if numbers == []:
    #     return False

    # evens = 0
    # for n in numbers:
    #     if n % 2 == 0:
    #         evens += 1
            
    # if evens == 0:
    #     return False
    # else:    
    #     return evens % 2 == 0
    
    #Third we can reduce the for loop function above through the use of Pytonic code or idiomatic Python as show below:
    # First part of the loop
    evens = sum([1 for n in numbers if is_even(n)])
    
    # Second part or return
    return False if evens == 0 else is_even(evens)  
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "Only one even number"
assert even_number_of_evens([1, 3, 9]) == False, "Three odd numbers"

print("All tests passed!")