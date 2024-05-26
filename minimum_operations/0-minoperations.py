#!/usr/bin/python3
"""Module for task 0
"""


def minOperations(n):
     """Calculate the fewest number of operations needed to result in exactly n H characters in the file."""


 if n < 2:
        return 0

# If n is less than 2 ,the operation will not work

 operations = 0
    divisor = 2

while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


# Here's an example 

print(minOperations(9))

# the example above prints 6
