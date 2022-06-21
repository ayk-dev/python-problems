def format_name(first, last):
    """
    :param first: first name
    :param last: last name
    :return: formatted string in title case
    """
    return first.title() + " " + last.title()


f_name = input("Enter first name: ")
l_name = input("Enter last name: ")

print(format_name(f_name, l_name))