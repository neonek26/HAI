import math

def scientific_calculator():
    print("Scientific Calculator")
    print("Enter 'quit' to exit")

    while True:
        user_input = input("Enter an expression: ")

        if user_input == 'quit':
            break

        try:
            result = eval(user_input)
            print(f"Result: {result}")
        except:
            print("Invalid expression")

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def main():
    scientific_calculator()

if __name__ == '__main__':
    main()
