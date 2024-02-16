#Callback function example
def do_operation(x, y, callback):
    result = x + y
    callback(result)

def print_result(result):
    print("The result is:", result)

do_operation(5, 3, print_result)
