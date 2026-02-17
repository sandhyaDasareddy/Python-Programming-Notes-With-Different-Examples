# Static variable example

class Employee:
    
    # Static (class) variable (shared by all objects)
    company = "TCS"
    
    def __init__(self, name, age, emp_id):
        # Instance variables (unique for each object)
        self.name = name
        self.age = age
        self.emp_id = emp_id
        
    def display_info(self):
        # Accessing static variable using class name (best practice)
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.emp_id}, Company: {Employee.company}")
        

def main():
    # Creating first object
    e1 = Employee("Priya", 24, 25001)
    e1.display_info()
    
    # __dict__ shows instance variables of e1 in dictionary form
    print("e1 instance variables:", e1.__dict__)
    
    # Creating second object
    e2 = Employee("Rohit", 42, 20050)
    e2.display_info()
    
    # __dict__ shows instance variables of e2
    print("e2 instance variables:", e2.__dict__)

    # Class __dict__ shows all class-level data
    # (static variables, methods, built-in attributes)
    print("Employee class dictionary:", Employee.__dict__)
    print(Employee.company)


# Main execution
if __name__ == "__main__":
    main()
