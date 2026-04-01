print("--- Simple To-Do List App ---")
tasks = []

while True:
    print("\nOptions:  1. Add Task   2. View Tasks   3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        new_task = input("Enter the task description: ")
        tasks.append(new_task)
        print(f" '{new_task}' added to your list.")
    
    elif choice == '2':
        print("\n--- Your Tasks ---")
        if not tasks:
            print("No tasks yet! You're all caught up.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
        print("------------------")
        
    elif choice == '3':
        print("Exiting To-Do List App. Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")