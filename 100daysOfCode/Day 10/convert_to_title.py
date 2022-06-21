def format_name(first, last):
  return first.title() + " " + last.title()


f_name = input("Enter first name: ")
l_name = input("Enter last name: ")

print(format_name(f_name, l_name))