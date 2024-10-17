#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    """
    Calculates the minimum number of operations required to achieve exactly `n` 'H' characters.
    
    :param n: The target number of 'H' characters.
    :return: The minimum number of operations needed, or 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1
    
    return operations

