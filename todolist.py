
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def edit(self, new_description, new_priority):
        self.description = new_description
        self.priority = new_priority



class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        self.tasks.append(Task(description, priority))
        print("Task added successfully!!")

    def edit_task(self, index, new_description, new_priority):
        if 0 <= index < len(self.tasks):
            self.tasks[index].edit(new_description, new_priority)
        print("Task edited successfully.")
      
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        print("Task marked as completed!!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for ix, task in enumerate(self.tasks):
                print(f"{ix}. {task}")
            print()


def main():
    todo_list = ToDoList()

    while True:
        print("\n To-Do List Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
                description = input("Enter task description: ")
                priority = input("Enter priority (high/medium/low): ")
                todo_list.add_task(description, priority)      
        elif choice == "2":
                index = int(input("Enter task number to edit: "))
                new_description = input("Enter new description: ")
                new_priority = input("Enter new priority: ")
                todo_list.edit_task(index, new_description, new_priority)
        elif choice == "3":
                index = int(input("Enter task number to mark as completed: "))
                todo_list.mark_task_completed(index)
        elif choice == "4":
                print("\nYour To-Do List:")
                todo_list.view_tasks()
        else: 
            choice == "5"
            print("exit")
        
main()
    





     


