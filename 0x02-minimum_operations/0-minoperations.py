#!/usr/bin/env python3
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
    number_of_operations = 0
    if n < 1:
        return 0
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
            n = int(math.sqrt(n))
            number_of_operations += n
    number_of_operations += n
    return number_of_operations


def isPrime(num):
    """
    Checks if a number is prime.
    """
    if num == 2 or num == 1 or num == 5 or num == 3:
        return True
    if num % 2 == 0 or addDigits(num) % 3 == 0 or num % 5 == 0:
        return False
    if (int(math.sqrt(num))) ** 2 != num:
        return True
    return False


def addDigits(num):
    """
    Adds the digits in a number.
    """
    sum_of_digits = 0
    while num != 0:
        sum_of_digits += num % 10
        num = num // 10

    return sum_of_digits
