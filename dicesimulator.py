import random


def die_face_generator(digit: int) -> str:
    """
    Function to print out basic render of a die face, of value equal to digit. If digit is not an integer between 1
    and 6, function will print a warning.
    :param digit: Any integer.
    :return: str
    """
    full_line = "-----------"
    middle_line = "|         |"
    one_dot = "|    o    |"
    two_dot = "|  o   o  |"

    if digit == 1:
        face_string = full_line + '\n' + middle_line + '\n' + one_dot + '\n' + middle_line + '\n' + full_line
    elif digit == 2:
        face_string = full_line + '\n' + middle_line + '\n' + two_dot + '\n' + middle_line + '\n' + full_line
    elif digit == 3:
        face_string = full_line + '\n' + one_dot + '\n' + one_dot + '\n' + one_dot + '\n' + full_line
    elif digit == 4:
        face_string = full_line + '\n' + two_dot + '\n' + middle_line + '\n' + two_dot + '\n' + full_line
    elif digit == 5:
        face_string = full_line + '\n' + two_dot + '\n' + one_dot + '\n' + two_dot + '\n' + full_line
    elif digit == 6:
        face_string = full_line + '\n' + two_dot + '\n' + two_dot + '\n' + two_dot + '\n' + full_line
    else:
        face_string = "This number doesn't exist on a regular die..?"

    return face_string


if __name__ == '__main__':

    print("This is a die-rolling simulator. First roll:")

    while True:
        x = random.randint(1, 6)

        face = die_face_generator(x)
        print(face)
        print()

        command = input("r: roll again; q: quit\n")

        if command == 'q':
            print("Quitting...")
            break
        elif command == 'r':
            print("Rolling...")
            continue
        else:
            print("Entry not recognised. Quitting...")
            break
