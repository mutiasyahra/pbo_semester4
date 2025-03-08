# Employee Management System (Hierarchical & Method Overriding)
# Class: Employee, Manager, Engineer, Intern
# Attributes: name, id, salary
# Methods: calculate_salary(), show_details()

class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def show_details(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: ${self.calculate_salary():.2f}"


class Manager(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        bonus = 0.20 * self.base_salary  # 20% bonus for Manager
        return self.base_salary + bonus


class Engineer(Employee):
    def __init__(self, name, emp_id, base_salary):
        super().__init__(name, emp_id, base_salary)

    def calculate_salary(self):
        performance_bonus = 0.10 * self.base_salary  # 10% performance bonus for Engineer
        return self.base_salary + performance_bonus


class Intern(Employee):
    def __init__(self, name, emp_id):
        super().__init__(name, emp_id, 1000)  # Fixed stipend for Interns

    def calculate_salary(self):
        return self.base_salary  # Interns only get the fixed stipend


# Main program to manage employees
employees = []

while True:
    print("--Menu--")
    print("1. List Employees")
    print("2. Add Employee")
    print("3. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        for index, employee in enumerate(employees):
            print(f"{index} - {employee.show_details()}")

    elif menu == "2":
        emp_type = input("Choose employee type (1: Manager, 2: Engineer, 3: Intern): ")
        name = input("Insert name: ")
        emp_id = input("Insert employee ID: ")
        
        if emp_type == "1":
            base_salary = float(input("Insert base salary: "))
            employees.append(Manager(name, emp_id, base_salary))
        elif emp_type == "2":
            base_salary = float(input("Insert base salary: "))
            employees.append(Engineer(name, emp_id, base_salary))
        elif emp_type == "3":
            employees.append(Intern(name, emp_id))
        else:
            print("Invalid employee type!")

    elif menu == "3":
        break

    else:
        print("Invalid choice")