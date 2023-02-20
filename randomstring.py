# import module
import random

# generate random list of integers
listOfInts = [random.randint(0, 20) for i in range(1000)] 

# print the list
for i in listOfInts:
    print(i)

# define a function
def random_function():
    # generate random number
    random_num = random.randint(0, 20)
    return random_num

# call the function and print the result
output = random_function()
print(output)

# generate a random string
random_string = ""
for i in range(20):
    random_string += random.choice("abcdefghijklmnopqrstuvwxyz")

# print the string
print(random_string)