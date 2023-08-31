# The main file we'll work with
while True:
    user_action = input(u"Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as fl:
                todos = fl.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1} - {item}")
            print(f"Length is, {len(todos)}")

        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the to-do to complete: "))

            with open('todos.txt', 'r') as fl:
                todos = fl.readlines()

            todos.pop(number - 1)

            with open('todos.txt', 'w') as fl:
                fl.writelines(todos)

            print(f"The item with index {number} was deleted")
        case 'edit':
            number = input("Number of the to-do to edit: ")

            with open('todos.txt', 'r') as fl:
                todos = fl.readlines()

            todos[int(number) - 1] = input("Enter a to-do replacement: ")

            with open('todos.txt', 'w') as fl:
                fl.writelines(todos)

            print("Your to-do updated!")
        case random_string:
            print("Hey, you entered an unknown command")
print("Bye")
