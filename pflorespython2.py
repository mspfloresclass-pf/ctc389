#Patricia Flores


def rectangle_function (length, height):
    area = length * height
    return area
userinput_length =float(input("Enter the base of the rectangle:"))
userinput_height =float(input("Enter the height of the rectangle:"))

output = rectangle_function (userinput_length, userinput_height)

print("The area of the rectangle is", output)
