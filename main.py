# The main file we'll work with 
todos = []

while True:
    user_action = input(u"Type add or show or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
