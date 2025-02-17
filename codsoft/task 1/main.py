tasklist =[]


def addtask():
    task = input("Enter your task: ")
    tasklist.append(task)
    # print(task, "is added to list")
    print(f"{task} is added to list")


def deletetask():
    delete_task = int(input("Enter s.no of the task you want to delete: "))
    if delete_task <= len(tasklist):
        fix = delete_task - 1
        tasklist.pop(fix)
        print(f"{delete_task} number task is deleted from list")
    else:
        print(f"{delete_task} number task is not in the list")
        print("check your To Do list")


def viewtask():
    print("Your To Do list is: ")
    for i in range(0,len(tasklist)):
        print(f"{i+1}. {tasklist[i]}")



if __name__ == "__main__":
    print("Your To DO list is waiting...")
    print("-------------------------------")
    print("Enter \"1\" for task entry")
    print("Enter \"2\" to delete task when completed")
    print("Enter \"3\" to view tasks")
    print("Enter \"4\" for QUIT")
    
    while True:
        choice = input("Enter number: ")
        if choice == "1":
            addtask()
        elif choice == "2":
            deletetask()
        elif choice == "3":
            viewtask()
        elif choice == "4":
            break
        else:
            print("Invalid number.")