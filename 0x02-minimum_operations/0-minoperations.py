#!/usr/bin/python3
"""
Minimum operations.
"""
import math


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    The only operations allowed are 'copy all' and 'paste'.
    """
    if n <= 1:
        return 0

    number_of_operations = 0

    while isPrime(n) is False:
        if n % 2 == 0:
            number_of_operations += 2
            n = n // 2
        elif n % 3 == 0:
            number_of_operations += 3
            n = n // 3
        elif n % 5 == 0:
            number_of_operations += 5
            n = n // 5
        else:
            for number in range(2, int(math.sqrt(n)) + 1):
                if n % number == 0:
                    n = n // number
                    number_of_operations += number
                    break
    number_of_operations += n
    return number_of_operations


def isPrime(num):
    """
    Checks if a number is prime.
    """
    if num in [1, 2, 3, 5]:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    # If the number is divisible by any of the prime numbers
    # less than its square root,
    # it is not a prime number; otherwise, it is prime.
    for number in range(2, int(math.sqrt(num)) + 1):
        if num % number == 0:
            return False
    return True
