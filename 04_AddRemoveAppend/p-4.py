EMPNAME = []
def display_menu():
    print("\nEmployee Name Management System")
    print("1. Add Employee Name")
    print("2. Remove Employee Name")
    print("3. Append Employee Name")
    print("4. Display Employee Names")
    print("5. Exit")
def add_employee_name():
    name = input("Enter employee name to add: ")
    EMPNAME.append(name)
    print(f"Employee name '{name}' added successfully!")
def remove_employee_name():
    name = input("Enter employee name to remove: ")
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Employee name '{name}' removed successfully!")
    else:
        print(f"Employee name '{name}' not found!")
def append_employee_name():
    name = input("Enter employee name to append: ")
    EMPNAME.append(name)
    print(f"Employee name '{name}' appended successfully!")
def display_employee_names():
    print("\nEmployee Names:")
    for i, name in enumerate(EMPNAME, start=1):
        print(f"{i}. {name}")
def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee_name()
        elif choice == 2:
            remove_employee_name()
        elif choice == 3:
            append_employee_name()
        elif choice == 4:
            display_employee_names()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")
if __name__ == "__main__":
    main()