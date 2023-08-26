# The main file we'll work with
while True:
    user_action = input(u"Type add, show, complete, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ") + "\n"
            file = open('todos.txt', 'r')

            todos = file.readlines()
            todos.append(todo)
            file.close()

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index + 1} - {item}")
            print(f"Length is, {len(todos)}")
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the to-do to complete: "))
            file = open('todos.txt', 'r')
            todos = file.readlines()
            todos.pop(number - 1)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            print(f"The item with index {number} was deleted")
        case 'edit':
            number = input("Number of the to-do to edit: ")
            file = open('todos.txt', 'r')
            todos = file.readlines()
            todos[int(number) - 1] = input("Enter a to-do replacement: ")
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            print("Your to-do updated!")
        case random_string:
            print("Hey, you entered an unknown command")
print("Bye")
