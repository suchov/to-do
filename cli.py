# The main file we'll work with
# from functions import get_todos, write_todos

import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, complete, edit or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")

        print(f"Length is, {len(todos)}")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"The item with index {number} was deleted")
        except ValueError:
            print("There is no item with this number")
            continue
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            todos[int(number) - 1] = input("Enter a to-do replacement: ")

            functions.write_todos(todos)

            print("Your to-do updated!")

        except IndexError:

            print("There is no item with this number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid, pls type valid command")

print("Bye")
