# The read and write functions for the todos app
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """The function that extract todos from the  file todos.txt is a default"""
    with open(filepath) as file:
        todos_funtion = file.readlines()
    return todos_funtion


def write_todos(todos_arg, filepath='todos.txt'):
    """The function that writes todos to txt file todos.txt is a default"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
