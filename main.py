class Todo:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.live = True

    def __str__(self):
        return f"Name: {self.name}\nDesription: {self.description}\nLive: {self.live}"


class Todos:

    def __init__(self):
        self.todo_list = []

    def add_todo(self):
        print("\n")
        name = input("Enter name of todo: ")
        desc = input("Enter description of todo: ")
        self.todo_list.append(Todo(name, desc))
        print(f"{name} has sucessfully been added to the todo list")

    def remove_todo(self):
        while True:
            try:
                todo = int(input("\nInput the number of a todo to remove: "))
                if todo > len(self.todo_list - 1) or todo != 0:
                    self.todo_list.pop(todo - 1)
                    print(f"Todo has been removed")
                    break
            except:
                print("Invalid input.")
                continue

    def complete_todo(self):
        while True:
            try:
                todo = int(input("\nInput the number of a todo to complete: "))
                if todo > (len(self.todo_list)) - 1 or todo != 0:
                    self.todo_list[todo - 1].live = False
                    break
                else:
                    continue
            except:
                print("Invalid input.\n")

    def view_todos(self):
        print("\n")
        for index, item in enumerate(self.todo_list):
            if item.live == True:
                print(f"{index + 1}. {item.name}, {item.description}")

    def view_comp_todos(self):
        print("\n")
        for index, item in enumerate(self.todo_list):
            if item.live == False:
                print(f"{index + 1}. {item.name}, {item.description}")


todo_list = Todos()

while True:
    print("\n")
    print("TODO LIST\n")
    print("please choose an option.\n")
    print(
        "\t1: Create a todo\n\t2: Complete a todo\n\t3: Remove a todo\n\t4: View live todo list\n\t5: View completed todos\n\t6: Exit\n"
    )

    try:
        user_input = int(input("Input number of selection: "))

        match user_input:
            case 1:
                todo_list.add_todo()
            case 2:
                todo_list.complete_todo()
            case 3:
                todo_list.remove_todo()
            case 4:
                todo_list.view_todos()
            case 5:
                todo_list.view_comp_todos()
            case 6:
                break
    except:
        print("Invalid option.")
