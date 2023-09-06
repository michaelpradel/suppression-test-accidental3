""" Toy module """

def hello():
    # pylint: disable=undefined-variable
    """ Hello function """
    name = the_name
    print(f"Hello, {name}!")
    name = another_name
    print(f"Hello, {name}!")
