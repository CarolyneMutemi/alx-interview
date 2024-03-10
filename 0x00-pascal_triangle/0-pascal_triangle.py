#!/usr/bin/python3
"""
Creating a Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Takes in a row number and returns the list of lists of numbers in each row.
    Args:
        n - the row number starting from 1(first row);
    Return:
        List of lists of numbers in each row.
    """

    whole_triangle_list = []
    current_row = [1]  # Initialized to the first row.
    whole_triangle_list.append(current_row)
    previous_row = current_row
    current_row_number = 1

    if n <= 0:
        return []
    while current_row_number < n:
        current_row = get_current_row(current_row_number, previous_row)
        whole_triangle_list.append(current_row)
        previous_row = current_row
        current_row_number += 1

    return whole_triangle_list


def get_current_row(current_row_number, previous_row):
    """
    Gets the current row numbers and returns a list of them.
    Args:
        current_row_number = the current row number.
        previous_row - previous row in the triangle.
    Return:
        list of numbers in the current row.
    """

    current_number_index = 0
    current_row = []

    while current_number_index <= current_row_number:
        if current_number_index in (0, current_row_number):
            current_number = 1
        else:
            sum_of_numbers_above = previous_row[
                current_number_index - 1] + previous_row[current_number_index]
            current_number = sum_of_numbers_above
        current_row.append(current_number)
        current_number_index += 1

    return current_row
