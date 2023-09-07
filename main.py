# The main file we'll work with
def get_todos(filepath='todos.txt'):
    """The function that extract todos from the  file todos.txt is a default"""
    with open(filepath) as file:
        todos_funtion = file.readlines()
    return todos_funtion


def write_todos(todos_arg, filepath='todos.txt'):
    """The function that writes todos to txt file todos.txt is a default"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, complete, edit or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")

        print(f"Length is, {len(todos)}")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todos.pop(number - 1)

            write_todos(todos)

            print(f"The item with index {number} was deleted")
        except ValueError:
            print("There is no item with this number")
            continue
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            todos[int(number) - 1] = input("Enter a to-do replacement: ")

            write_todos(todos)

            print("Your to-do updated!")

        except IndexError:

            print("There is no item with this number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid, pls type valid command")

print("Bye")
