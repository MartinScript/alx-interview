#!/usr/bin/python3

# import asyncio
# from msilib.text import tables
# import time
# import cProfile
# from concurrent import futures

#[1,]
#[1,1]
#[1,2,1]
#[1,3,3,1]
#[1,4,6,4,1]
#[1,5,10,10,5,1]
#[1,6,15,20,15,6,1]

#solution 1
"""def pascal_generator(lst):
  for i in range(len(lst)-1):
    yield lst[i] + lst[i+1]"""

#first implementation but not efficient
"""def pascal_triangle(n):
  prev_lst = [1,1]
  triangle = [[1]]
  for i in range(n-1):
    prev_lst = [1] + [j for j in pascal_generator(prev_lst)] + [1]
    triangle.append(prev_lst)
  
  return triangle"""
  
def pascal_triangle(n):
  row = [1]
  triangle = [[1]]
  if n <= 0:
    return [[]]
  for i in range(n-1):
    row = [i+j for i,j in zip([0] + row, row + [0])]
    triangle.append(row)
  return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(10))