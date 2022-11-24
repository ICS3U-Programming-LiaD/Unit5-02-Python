
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.24th, 2022
# This program finds the area of a
# triangle with user input

# Defines the Function
def calc_area(base, height):
    # Formula for the area of a triangle
    area = base * height / 2
    return print(" The area of the triangle is {}㎠".format(area))


def main():
    # Getting the base and height from the user
    user_input_base = input("Enter the length of the base: ")
    user_input_height = input("Enter the height of the triangle: ")

    try:
        # Checking if it is an actual number
        user_input_base = float(user_input_base)
        user_input_height = float(user_input_height)
        # Makes sure that it is a positive number
        if user_input_base < 0 or user_input_height < 0:
            print("please enter a positive number")

        else:
            # Calls the function
            calc_area(user_input_base, user_input_height)
    except ValueError:
        print("please input a number")


if __name__ == "__main__":
    main()
