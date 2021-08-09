from LinearAlgebra import *
from typing import Tuple, Callable

Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
    """
    Return tuple(number of rows, number of columns)
    :param A: Matrix
    :return: returns tuple of lengths
    """
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0

    return num_rows, num_cols


def get_row(A: Matrix, i: int) -> Vector:
    """
    Return row and ith index
    :param A: Matrix
    :param i: ith index
    :return: return vector of row i
    """

    return A[i]


def get_col(A: Matrix, i: int) -> Vector:
    """
    Return column and ith index
    :param A: Matrix
    :param i: ith index
    :return: return vector of column i
    """
    return [row[i] for row in A]


def make_matrix(rows: int, cols: int, entry_fn: Callable) -> Matrix:
    """
    Makes a matrix, based on input function which should take row and column index as inputs
    :param rows: number of rows
    :param cols: number of cols
    :param entry_fn: Function that takes row and col indicies
    :return: constructed matrix
    >>> make_matrix(5, 5, lambda i, j: 1 if i == j else 0)
    [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(cols)]      # [entry_fn(i, 0), ..., entry_fn(i, cols-1)]
             for i in range(rows)]     # create 1 list for each i (row)


def identity_matrix(n: int) -> Matrix:
    """
    Returns an identity matrix that n x n elements
    :param n: size of identity matrix
    :return: identity matrix
    >>> identity_matrix(6)
    [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


if __name__ == '__main__':

    print(make_matrix(6, 6, lambda i, j: 1 if i == j else 0))