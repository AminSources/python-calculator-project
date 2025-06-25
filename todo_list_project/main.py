# ? python todo list (command-line) project
# ? developed by Mohammad Amin Farshbaf. 2025-6-26 12:14 AM

# * app variables
tasksList = []
getKeys = ("all", "title", "description", "date", "status")


# * app classes
class Task:
    def __init__(self, title, description, date, status):
        self.title = title
        self.description = description
        self.date = date
        self.status = status


# * app functions
def add_task(title, description, date, status):
    tasksList.append(Task(title, description, date, status))


def remove_task(index):
    del tasksList[index]


def update_task(index, title, description, date, status):
    tasksList[index] = Task(title, description, date, status)


def get_task(getBy):
    if len(tasksList) > 0:
        index = 0
        if getBy in getKeys and getBy != "all":
            for tasks in tasksList:
                index += 1
                print(
                    f"\ntask index: {index}\n{getBy}: {getattr(tasks, getBy)}\n==========="
                )

        elif getBy == "all":
            for tasks in tasksList:
                index += 1
                print(
                    f"\ntask index: {index}\ntitle: {tasks.title}\ndescription: {tasks.description}\ndate: {tasks.date}\nstatus: {tasks.status}\n============"
                )
        else:
            print("Invalid operation. Please try again.")
    else:
        print("No tasks found.")


def run_app():
    while True:
        action = input("Enter task operation (add, remove, update, get, exit): ")
        if action == "add":
            add_task(
                input("Enter task title: "),
                input("Enter task description: "),
                input("Enter task date (yyyy-mm-dd): "),
                input("Enter task status (completed/incomplete): "),
            )
            print("added successfuly")
        elif action == "remove":
            userInput = int(input("Enter task index to remove: "))
            remove_task(userInput - 1)
            print("removed successfuly")

        elif action == "update":
            userInput = int(input("Enter task index to update: "))
            update_task(
                userInput - 1,
                input("Enter new task title: "),
                input("Enter new task description: "),
                input("Enter new task date (yyyy-mm-dd): "),
                input("Enter new task status (completed/incomplete): "),
            )
            print("updated successfuly")

        elif action == "get":
            while True:
                userInput = input(
                    "Enter operation type (all, title, description, date, status, back): "
                )
                if userInput in getKeys:
                    get_task(userInput)
                    break
                elif userInput == "back":
                    break
                else:
                    print("Invalid operation. Please try again.")

        elif action == "exit":
            break
        else:
            print("Invalid operation. Please try again.")


run_app()
