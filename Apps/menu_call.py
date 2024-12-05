
def Call():
    print("\n\n    1. Main Menu\n    2. Exit")
    key = int(input("\n    Choose One of the above options : "))

    if key == 2:
        exit()
    elif key != 1:
        print("Invalid Input")