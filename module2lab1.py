"""
CTEC 121
Edward LaManna
Module 3 lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

"""
def main():

    print("\nBoolen literals")
    print(True)
    print(False)
    print(type(True))
    print()

    print("relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 !- 5", 3 != 5)
    print()

    x = 3
    y = 5
    print("using variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    # simple if statement
    print("simple if statements")

    print("x:", x, "y:", y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statement
    print("if/else stement")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")
    print()
    print("new value of x")
    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

main()

    """


def main():
    """
    # exercise 3-1
    for i in range(1, 11):
        if (i % 2) == 0:
            outputstring = "even"
        else:
            outputstring = "odd"
        print(i, outputstring)

    print()
    print("names")
    print()
    # alphabetize names
    name = "Bill"
    firstletterofname = "B"

    print("Multi-way if example")
    if firstletterofname == "A":
        print("A")
    elif firstletterofname == "B":
        print("B")
    elif firstletterofname == "C":
        print("C")
       # ....
    elif firstletterofname == "Y":
        print("Y")
    else:  # default case: name starts with "z"
        print("Z")

    print()
    """
    try:
        print(4/0)
    except:
        print("\nThere was a deivide by zero error. exiting\n")
        exit()


main()
