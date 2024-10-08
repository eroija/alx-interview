#!/usr/bin/python3
"""A module for working with Pascal's triangle."""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing thr Pascal's triangle of
    a given integer.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
