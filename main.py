# The main file we'll work with 
todos = []

while True:
    user_action = input(u"Type add or show: ")
    match user_action:
        case 'add':
            todo = input("Enter a to-do: ")
            todos.append(todo)
        case 'show':
            print(todos)
