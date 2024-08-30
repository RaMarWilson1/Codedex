import math

while True:
    print("1:square\n2:circle\n3:rectangle\n4:triangle\n5: end ")
    shape = int(input("Enter the number of the shape\n"))
    print("Which shape: ",shape)
    if shape == 1:
        x = int(input("Enter the length of the square"))
        print("Sides:",x)
        print("The area square of the square is", x*x)
    elif shape == 2:
        x = int(input("Enter the radius of the circle"))
        print("r:",x)
        print ("The  area circle is", (math.pi*(x*x)))
    elif shape == 3:
        x = int(input("Enter the length of the rectangle"))
        y = int(input("Enter the width of the rectangle"))
        print("length:",x)
        print("width:",y)
        print("The area of the rectangle is",x*y)
    elif shape == 4:
        h = int(input("Enter the height of the triangle"))
        b=int(input("Enter the base of the triangle"))
        print("Base:",b)
        print("Height:",h)
        print ("The area of the triangle is",((1/2)*(h*b)))
    elif shape==5:
        print("Thank you for using Area calculator\n Goodbye")
        break
    else :(print("Please enter a number between 1 and 5"))

