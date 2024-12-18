from warnings import showwarning

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input('Enter a todo: ') + '\n'

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            # With context manager
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                # file.close()  You DONT need close() with context manager its implied.  If program crash, file is closed

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []

            # for item in todos:
            #    new_item = item.strip('\n')
            #    new_todos.append(new_item)

            # Better - List Comprehension
            # [item.strip('\n')] for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            removed = todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {removed.strip('\n')} was removed from the list"
            print(message)

        case 'exit':
            break


