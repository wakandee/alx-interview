#!/usr/bin/python3
"""
Minimum Operations Module
This script calculates the minimum number of operations
needed to achieve exactly `n` 'H' characters 
using a combination of copy and paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly `n` 'H' characters.
    
    :param n: The target number of characters.
    :return: The minimum number of operations required, or 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    
    # Continuously divide n by its smallest prime factors to count operations
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1
    
    return operations

