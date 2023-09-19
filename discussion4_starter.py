class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE
    def __init__(self, width, height):
        self.wid = width
        self.ht = height



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    # YOUR CODE HERE
    def __str__(self):
        return "A rectangle with width " + str(self.wid) + " and height " + str(self.ht)



    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    # YOUR CODE HERE
    def verify_input(self):
        if self.wid > 0 and self.ht > 0:
            return True
        else:
            return False


    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    # YOUR CODE HERE
    def area(self):
        if not self.verify_input():
            return "Invalid input"
        else:
            return self.wid * self.ht



    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    # YOUR CODE HERE
    def perimeter(self):
        if not self.verify_input():
            return "Invalid input"
        else:
            return (self.wid + self.ht) * 2
        
    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()
