import math

class Circle:
    shapes_created = 0

    def __init__(self, radius: float):
        if not self.is_valid_dimension(radius):
            raise ValueError("Radius must be positive.")
        self.radius = radius
        Circle.shapes_created += 1

    def area(self) -> float:
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)

    def __str__(self) -> str:
        return f"Circle(r={self.radius})"

    @staticmethod
    def cm_to_inch(cm: float) -> float:
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val: float) -> bool:
        return val > 0

    @classmethod
    def total_created(cls) -> str:
        return f"Circles created: {cls.shapes_created}"


class Rectangle:
    shapes_created = 0

    def __init__(self, width: float, height: float):
        if not self.is_valid_dimension(width) or not self.is_valid_dimension(height):
            raise ValueError("Dimensions must be positive.")
        self.width = width
        self.height = height
        Rectangle.shapes_created += 1

    def area(self) -> float:
        return round(self.width * self.height, 2)

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 2)

    def is_square(self) -> bool:
        return self.width == self.height

    def __str__(self) -> str:
        return f"Rectangle({self.width} x {self.height})"

    @staticmethod
    def cm_to_inch(cm: float) -> float:
        return round(cm * 0.3937, 3)

    @staticmethod
    def is_valid_dimension(val: float) -> bool:
        return val > 0

    @classmethod
    def total_created(cls) -> str:
        return f"Rectangles created: {cls.shapes_created}"


# --- Interactive User Input Menu ---
def main():
    print("=== Welcome to the Shape Calculator ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Create a Circle")
        print("2. Create a Rectangle")
        print("3. Convert cm to inches")
        print("4. View Total Shapes Created")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        try:
            if choice == "1":
                r = float(input("Enter circle radius: "))
                my_circle = Circle(r)
                print(f"\n✅ Success: {my_circle}")
                print(f"   Area: {my_circle.area()}")
                print(f"   Perimeter: {my_circle.perimeter()}")
                
            elif choice == "2":
                w = float(input("Enter rectangle width: "))
                h = float(input("Enter rectangle height: "))
                my_rect = Rectangle(w, h)
                print(f"\n✅ Success: {my_rect}")
                print(f"   Area: {my_rect.area()}")
                print(f"   Perimeter: {my_rect.perimeter()}")
                print(f"   Is Square?: {my_rect.is_square()}")
                
            elif choice == "3":
                cm = float(input("Enter centimeters to convert: "))
                # Using static method directly from the class
                print(f"\n📏 {cm} cm = {Circle.cm_to_inch(cm)} inches")
                
            elif choice == "4":
                print(f"\n📊 {Circle.total_created()}")
                print(f"📊 {Rectangle.total_created()}")
                
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\n❌ Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError as e:
            # Catches both string-to-float conversion errors AND our custom shape validation errors
            print(f"\n❌ Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()