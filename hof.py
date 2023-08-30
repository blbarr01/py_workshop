def greet(name):
    return f"Hello, {name}!"

# Functions can be assigned to variables
my_function = greet

# Functions can be passed as arguments
def apply_function(func, value):
    return func(value)

result = apply_function(my_function, "Alice")  # result = "Hello, Alice!"

# Functions can be returned from functions
def get_function():
    return greet

returned_function = get_function()
greeting = returned_function("Bob")  # greeting = "Hello, Bob!"
