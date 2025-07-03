import csv
from tabulate import tabulate
import os

def get_data():
    # Load data from the CSV file
    if not os.path.exists("todolist.csv"):
        return [], ['serial no', 'todo', 'status']
    
    with open("todolist.csv", "r", newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        if not data:
            return [], ['serial no', 'todo', 'status']
        return data[1:], data[0]  

def save_data(rows, headers):
    with open("todolist.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

def create():
    rows, headers = get_data()
    sno = len(rows) + 1
    todo = input("Enter a task to be added to the To-Do list: ")
    status = "pending"
    rows.append([sno, todo, status])
    save_data(rows, headers)
    print("Task added successfully!")

def update():
    rows, headers = get_data()
    if not rows:
        print("No tasks to update.")
        return
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    
    try:
        search = int(input("Enter the serial number you want to update: "))
        if 1 <= search <= len(rows):
            new_todo = input("Enter new task (leave blank to keep current): ")
            upd_status = input("Enter new status (pending/done): ")
            if new_todo:
                rows[search - 1][1] = new_todo
            if upd_status:
                rows[search - 1][2] = upd_status
            save_data(rows, headers)
            print("Task updated successfully!")
        else:
            print("Invalid serial number.")
    except ValueError:
        print("Invalid input.")

def track():
    rows, headers = get_data()
    if rows:
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No tasks in the list.")

# Main Program
print("To-Do List")
while True:
    print("Choose any option:")
    print("1. Create")
    print("2. Update")
    print("3. Track")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create()
        elif choice == 2:
            update()
        elif choice == 3:
            track()
        elif choice == 4:
            print("Exiting To-Do List program.")
            break
        else:
            print("Invalid option. Try again.")
    except ValueError:
        print("Please enter a valid number.")

    
    
