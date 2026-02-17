# Example program demonstrating instance variables and dynamic attributes

class Student:
    # Constructor to initialize instance variables
    def __init__(self, name, age, roll_no):
        self.name = name          # instance variable
        self.age = age            # instance variable
        self.roll_no = roll_no    # instance variable

    # Method to generate hall ticket
    def hall_ticket(self):
        print(f"Hall ticket for {self.name} with roll number {self.roll_no} is generated.")

    # Method to display student information
    # Note: branch and semester are added dynamically later
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, "
              f"Branch: {self.branch}, Semester: {self.semester}")


def main():
    # Creating object
    s1 = Student("Sandhya", 25, 101)

    # Adding new instance variables dynamically
    s1.branch = "Computer Science"
    s1.semester = 6

    # Accessing attributes directly
    print(s1.name)
    print(s1.branch)
    print(s1.semester)

    # Using setattr() to set attributes dynamically
    setattr(s1, "branch", "Computer Science")
    setattr(s1, "semester", 6)

    # Using getattr() to access attribute values
    print(getattr(s1, "name"))
    print(getattr(s1, "branch"))
    print(getattr(s1, "semester"))

    # Using hasattr() to check attribute existence
    print(hasattr(s1, "name"))     # True
    print(hasattr(s1, "gender"))   # False

    # __dict__ shows all instance variables in dictionary form
    print(s1.__dict__)

    # Accessing value from __dict__
    print(s1.__dict__['name'])


# Main execution
if __name__ == "__main__":
    main()

