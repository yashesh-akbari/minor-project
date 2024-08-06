todo_list = []

while True:
    if not todo_list:
        print("Your Todo list is empty")
    else:
        index=1
        for task in todo_list:
            print(f"{index}.{task}")
            index = index + 1
    
    print("options:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Quit")
    
    choice = input("Enter your choice (1,2 or 3): ")
    
    if choice == "1":
        print ("Adding Task")
        new_task = input(f"Enter your Todo:")
        todo_list.append(new_task)
        print(f"Task '{new_task} added to the Todo list'")
    elif choice == "2":
        if(todo_list==[]):
            print ("Enter a task for remove")
        else:
            print("Removing task")
            todo_list.pop()
            print(f"Task 'update Todo list {todo_list}'")
    elif choice == "3":
        print("Quitting")
        break
    else:
        print("You enter invaild option")