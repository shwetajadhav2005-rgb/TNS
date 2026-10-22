PI = 3.14159
def area_of_circle(radius):
     return PI * (radius ** 2)

def perimeter_of_rectangle(length, breadth):
     return 2*(length+breadth)

if __name__ == "__main__":
 print(f"Area of circle {area_of_circle(5)}")
print(f"perimeter_of_circle {perimeter_of_rectangle(3,2)} ")