"""
Main.py: The main file.
"""

from src import ExampleClass

def my_code(x_variable: int) -> int:
    """
    A function that takes x as an input and returns y as an output.
    """

    return x_variable * 3

my_example = ExampleClass()

print(my_example.start())

my_code(3)
