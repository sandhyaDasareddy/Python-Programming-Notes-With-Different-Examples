# Example program demonstrating a class with instance variables and methods

class Car:
    
    # Constructor - initializes instance variables
    def __init__(self):
        self.brand = "BMW"     # instance variable
        self.cc = 2100         # engine capacity
        self.color = "Blue"    # car color

    # Method to start the engine
    def start_engine(self):
        print("Engine is starting...")

    # Method to shift gear
    def shift_gear(self):
        print("Shifting gear...")

    # Method to accelerate the car
    def accelerate(self):
        print("Car is accelerating...")

    # Method to stop the engine
    def stop_engine(self):
        print("Engine is stopping...")


def main():
    # Creating an object of Car class
    c1 = Car()

    # Accessing instance variables
    print("Brand:", c1.brand)
    print("CC:", c1.cc)
    print("Color:", c1.color)

    # Calling methods
    c1.start_engine()
    c1.shift_gear()
    c1.accelerate()
    c1.stop_engine()


# Main execution
if __name__ == "__main__":
    main()
