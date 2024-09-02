#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed. The value should be greater than or equal to 0.

    Returns:
    int: The factorial of the input integer n. Factorial of n (n!) is defined as n * (n-1) * (n-2) * ... * 1. Factorial of 0 is 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ensure that the script is run with at least one argument
if len(sys.argv) != 2:
    print("Usage: python script.py <non-negative integer>")
    sys.exit(1)

# Compute the factorial of the input argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
