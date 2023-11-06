from package.math_operations import MathOperations 
from package.geometry import Geometry 
 
if __name__ == "__main__": 
    # Demonstrating MathOperations 
    result = MathOperations.add(5, 3) 
    print(f"5 + 3 = {result}") 
 
    result = MathOperations.subtract(10, 4) 
    print(f"10 - 4 = {result}") 
 
    # Demonstrating Geometry 
    area = Geometry.calculate_area(4, 6) 
    print(f"Area of a rectangle with length 4 and width 6: {area}") 
 
    perimeter = Geometry.calculate_perimeter(4, 6) 
    print(f"Perimeter of the same rectangle: {perimeter}") 
