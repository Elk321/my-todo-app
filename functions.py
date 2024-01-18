FILEPATH = "C:/Users/chene/Desktop/python/to_do_list/todos.txt"


def check_character(string, action, todos):
    """ Check if a string meets the conditions."""
    condition = False
    while True:
        # check if the string is empty or not
        if len(string) > 0:
            # check if the string is a digit
            if string.isdigit():
                # check if the number is contained in the list
                if 0 < int(string) <= len(todos):
                    condition = True
                else:
                    print("The number entered does not exist in the list.")
            else:
                print("The character entered is not a digit.")
        else:
            print("No number entered.")
        # check if the condition is true
        if not condition:
            string = input(f"Please enter the number of todo to {action}: ").strip()
        else:
            break
    return string


def cap_todo(string):
    """ Return a string with only the first letter
    capitalized and the other words untouched
    """
    string_list = string.split(" ")
    string_list[0] = string_list[0].title()
    return " ".join(string_list)


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of the
    to-do items.
    """
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


def period_check(string):
    """ Check if a string ends with period and
    if not add to it."""
    if string[-1] == ".":
        string = string + "\n"
    else:
        string = string + ".\n"

    return string


def update(window, todos):
    """" Update the window"""
    window["todos"].update(values=todos)
    window["todo"].update(value="")
