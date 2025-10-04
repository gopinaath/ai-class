def display_menu():
    print("\nGeometry Calculator\n")
    print("1. Calculate the Area of a Circle")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Triangle")
    print("4. Quit")


def calculate_circle_area():
    radius = float(input("\nEnter the radius of the circle: "))
    if radius < 0:
        print("Error: Radius cannot be negative.")
        return

    PI = 3.14159
    area = PI * radius * radius
    print(f"The area of the circle is: {area:.2f}")


def calculate_rectangle_area():
    length = float(input("\nEnter the length of the rectangle: "))
    if length < 0:
        print("Error: Length cannot be negative.")
        return

    width = float(input("Enter the width of the rectangle: "))
    if width < 0:
        print("Error: Width cannot be negative.")
        return

    area = length * width
    print(f"The area of the rectangle is: {area:.2f}")


def calculate_triangle_area():
    base = float(input("\nEnter the base of the triangle: "))
    if base < 0:
        print("Error: Base cannot be negative.")
        return

    height = float(input("Enter the height of the triangle: "))
    if height < 0:
        print("Error: Height cannot be negative.")
        return

    area = base * height * 0.5
    print(f"The area of the triangle is: {area:.2f}")


def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                calculate_circle_area()
            elif choice == 2:
                calculate_rectangle_area()
            elif choice == 3:
                calculate_triangle_area()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Error: Please enter a number between 1 and 4.")
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()