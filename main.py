# The main file we'll work with
todos = []

while True:
    user_action = input(u"Type add or show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                print(f"{index} - {item}")
        case 'exit':
            break
        case 'edit':
            number = input("Number of the to-do to edit: ")
            todos[int(number) + 1] = input("Enter a to-do replacement: ")
            print("Your to-do updated!")
        case random_string:
            print("Hey, you entered an unknown command")
print("Bye")
