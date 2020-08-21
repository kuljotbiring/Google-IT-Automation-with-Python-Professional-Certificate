# The parent_directory function returns the name of the directory that's located
# just above the current working directory

import os


def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join("./", "../")

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())
