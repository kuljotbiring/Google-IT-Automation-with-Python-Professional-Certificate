# the rearrange_name function swaps first & last names. It can match middle names, middle
# initials, as well as double surnames.
import re

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name=rearrange_name("Kennedy, John F.")
print(name)
