# The main file we'll work with
while True:
    user_action = input(u"Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todos.txt') as fl:
            todos = fl.readlines()

            todos.append(todo + '\n')

        with open('todos.txt', 'w') as fl:
            fl.writelines(todos)
            print(todos)

    elif 'show' in user_action:
        with open('todos.txt') as fl:
            todos = fl.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")
        print(f"Length is, {len(todos)}")

    elif 'complete' in user_action or 'delete' in user_action:
        number = int(input("Number of the to-do to complete: "))

        with open('todos.txt') as fl:
            todos = fl.readlines()

        todos.pop(number - 1)

        with open('todos.txt', 'w') as fl:
            fl.writelines(todos)

        print(f"The item with index {number} was deleted")
    elif 'edit' in user_action:
        number = int(user_action[5:])

        with open('todos.txt') as fl:
            todos = fl.readlines()

        todos[int(number) - 1] = input("Enter a to-do replacement: ")

        with open('todos.txt', 'w') as fl:
            fl.writelines(todos)

        print("Your to-do updated!")
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid, pls type valid command")
print("Bye")
