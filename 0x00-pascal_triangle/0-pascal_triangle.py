#!/usr/bin/python3
  
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of binomial coefficients. Each number is the sum of the two directly above it.
    The function accepts an integer n as input and returns a list of lists representing the Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    list: A list of lists representing Pascal's Triangle up to the nth row. If n is not a positive integer, an empty list is returned.

    Raises:
    ValueError: If n is not an integer.
    """
    try:
        n = int(n)
        row = [1]
        triangle = [[1]]
        if n <= 0:
            return [[]]
        for i in range(n-1):
            row = [i+j for i,j in zip([0] + row, row + [0])]
            triangle.append(row)
        
        return triangle
    except (ValueError, TypeError) as e:
        print("{0} is not an integer, argument must be an interger".format(n))
        return None

  
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


if __name__ == "__main__":
    print_triangle(pascal_triangle(7))