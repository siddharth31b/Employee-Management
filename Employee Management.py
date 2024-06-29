class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

class ManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            employee.display()

    def remove_employee(self, id):
        self.employees = [employee for employee in self.employees if employee.id != id]

    def update_employee(self, id, name=None, position=None, salary=None):
        for employee in self.employees:
            if employee.id == id:
                if name:
                    employee.name = name
                if position:
                    employee.position = position
                if salary:
                    employee.salary = salary

def main():
    system = ManagementSystem()

    while True:
        print("\n1. Add Employee\n2. View Employees\n3. Remove Employee\n4. Update Employee\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter ID: ")
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = input("Enter salary: ")
            system.add_employee(Employee(id, name, position, salary))
        elif choice == '2':
            system.display_employees()
        elif choice == '3':
            id = input("Enter ID of the employee to remove: ")
            system.remove_employee(id)
        elif choice == '4':
            id = input("Enter ID of the employee to update: ")
            name = input("Enter new name (leave blank to not change): ")
            position = input("Enter new position (leave blank to not change): ")
            salary = input("Enter new salary (leave blank to not change): ")
            system.update_employee(id, name if name else None, position if position else None, salary if salary else None)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()