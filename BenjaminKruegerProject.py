Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """This program serves as a calculator"""
... __author__ = "Benjamin Krueger"
... 
... import math
... import time
... 
... 
... def add(num1, num2):
...     """
... This function gets number 1 and adds it to number 2.
...     :param num1: first number the user is going to input
...     :param num2: second number the user in going to input
...     :return: the result of the addition of the two given numbers.
...     """
...     return num1 + num2
... 
... 
... def subtract(num1, num2):
...     """
... This function gets number 1 and subtracts it to number 2.
...     :param num1: first number the user is going to input
...     :param num2: second number the user in going to input
...     :return: The result of the subtraction
...     """
...     return num1 - num2
... 
... 
... def multiplication(num1, num2):
...     """
... This function gets number 1 and multiplies it for number 2.
...     :param num1: first number the user is going to input
...     :param num2: second number the user in going to input
...     :return: The result of the multiplication
...     """
...     return num1 * num2
... 
... 
... def division(num1, num2):
    """
This function gets number 1 and divides it for number 2.
    :param num1: The dividend
    :param num2: The divisor
    :return: The result of the division
    """
    return num1 / num2


def percentage(num1, num2):
    """
This function gets a first number and then multiplies it for 1/100 of the percentage you input.
    :param num1: The first number
    :param num2: The percentage
    :return: The multiplication between first number and percentage
    """
    return num1 * (num2 * 0.01)


def power(num1, num2):
    """
This function gets the first number and does the power to the second number.
    :param num1: The first number
    :param num2: The power
    :return: The result of the power
    """
    return num1 ** num2


def whole_num_division(num1, num2):
    """
This function makes a division and returns a whole number.
    :param num1: The dividend
    :param num2: The divisor
    :return: The result of the division as a whole number
    """
    return num1 // num2


def remainder(num1, num2):
    """
This function gets 2 numbers and gets the remainder of the division .
    :param num1: The dividend
    :param num2: The divisor
    :return: what is left after the division. If it is a perfect division it will return 0
    """
    return num1 % num2


def square_root(num1):
    """
This function returns the square root of the number you input.
    :param num1: The first number
    :return: THe result of the square root
    """
    return math.sqrt(num1)


def main():
    valid = True
    while valid:  # Loop that goes until a name is input

        name = input("What is your name?: ")

        if name.isalpha():  # Test to see if the input is alphabetic
            print("Hello " + name + "! Welcome to my calculator. This program will help you with everyday simple "
                                    "problems", end="!\n\n\n\n")
            valid = False  # stops the loop

        else:
            print("Invalid name. Try again.\n")
            continue

    intro = "\t*** Program Menu ***\n"
    catalog = "\t(1) - addition.\n" \
              "\t(2) - subtraction.\n" \
              "\t(3) - multiplication.\n" \
              "\t(4) - division.\n" \
              "\t(5) - percentage.\n" \
              "\t(6) - power.\n" \
              "\t(7) - whole division.\n" \
              "\t(8) - remainder.\n" \
              "\t(9) - square root.\n" \
              "\t(10) - And Or But Explanation\n" \
              "\t(0) - Exit\n"

    separation = ("=" * 69 + "\n\n")

    loop = 0
    while loop != 99:

        time.sleep(1)
        
        print(intro, catalog, sep="\n")
        choice = int(input("\n\nPlease select the function you want to use: "))

        if 0 <= choice < 11:  # checking to see if the choice is possible
            if choice == 1:
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                print(add(num1, num2))
                print(separation)

            elif choice == 2:
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                print(subtract(num1, num2))
                print(separation)

            elif choice == 3:
                num1 = float(input("Number 1: "))
                num2 = float(input("Number 2: "))
                print(multiplication(num1, num2))
                print(separation)

            elif choice == 4:
                num1 = float(input("Dividend: "))
                num2 = float(input("Divisor: "))
                print("{:.2f}".format(division(num1, num2)))
                print(separation)

            elif choice == 5:
                num1 = float(input("Number 1: "))
                num2 = float(input("Percentage: "))
                print(percentage(num1, num2))
                print(separation)

            elif choice == 6:
                num1 = float(input("Number 1: "))
                num2 = float(input("Power: "))
                print(power(num1, num2))
                print(separation)

            elif choice == 7:
                num1 = float(input("Dividend: "))
                num2 = float(input("Divisor: "))
                print(whole_num_division(num1, num2))
                print(separation)

            elif choice == 8:
                num1 = float(input("Dividend: "))
                num2 = float(input("Divisor: "))
                print(remainder(num1, num2))
                print(separation)

            elif choice == 9:
                test = 0
                while test == 0:
                    num1 = float(input("Number 1: "))
                    if num1 >= 0:
                        print("{:.3f}".format(square_root(num1)))  # Format tool to get only 3 decimals
                        test += 1
                        print(separation)

                    else:
                        print("You can't get the square root of a negative number.\nSelect another number.")

            elif choice == 0:
                for i in range(0, 5, 1):
                    print(i, ": Thank you for using the program.")
                loop = 99

            elif choice == 10:

                m = 6  # explanation of the use of AND, OR, NOT
                n = 3

                print("Lets designated M as 6 and N as 3\n\n"
                      "AND is used to compare 2 statements.\n"
                      "If both are true the boolean is se to TRUE\n"
                      "If one of the statements is false, the boolean is FALSE.")
                print("If X == Y and X > Y return 'True' else return 'False'")
                if m == n and m > n:
                    print(True)
                else:
                    print(False, "\n")

                print("OR is used to compare 2 statements.\n"
                      "If at least one of the statements is true, the boolean is TRUE.\n"
                      "If both statements are false, the boolean is FALSE.")
                print("If X == Y or X > Y return 'True' else return 'False'")
                if m == n or m > n:
                    print(True)
                else:
                    print(False, "\n")

                print("NOT is used to compare to statements.\n"
                      "If the statement is false, the boolean is TRUE.\n"
                      "If the statement is true, the boolean is FALSE.")
                print("If not X == Y ")
                if not m == n:
                    print(True, "\n")

                else:
                    print(False, "\n")

                time.sleep(3)
                print(separation)

            else:
                continue


if __name__ == '__main__':
    main()
