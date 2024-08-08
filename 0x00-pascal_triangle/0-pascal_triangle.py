#!/usr/bin/python3
"""
Generate Pascal's Triangle up to the nth row.

Pascal's Triangle is a triangular array of binomial coefficients. Each number is the sum of the two directly above it.
The function accepts an integer n as input and returns a list of lists representing the Pascal's Triangle up to the nth row."""
  
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of binomial coefficients. Each number is the sum of the two directly above it.
    The function accepts an integer n as input and returns a list of lists representing the Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows to generate in Pascal's Triangle. Must be a positive integer.

    Returns:
    list: A list of lists representing Pascal's Triangle up to the nth row. If n is not a positive integer, returns an empty list.
    """
    if type(n) is not int or n <= 0:
        return [[]]
    row = [1]
    triangle = [[1]]
    for i in range(n-1):
        row = [i+j for i,j in zip([0] + row, row + [0])]
        triangle.append(row)
        
    return triangle

#first implementation but not efficient
"""def pascal_generator(lst):
  for i in range(len(lst)-1):
    yield lst[i] + lst[i+1]"""

"""def pascal_triangle(n):
  prev_lst = [1,1]
  triangle = [[1]]
  for i in range(n-1):
    prev_lst = [1] + [j for j in pascal_generator(prev_lst)] + [1]
    triangle.append(prev_lst)
  
  return triangle"""