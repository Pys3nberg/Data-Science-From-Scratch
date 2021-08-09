from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """
    Adds two vectors of equal length together
    :param v: Vector v
    :param w: Vector w
    :return: Vector resulting from adding elements from each vector.
    >>> add([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    >>> add([7, 8, 9], [10, 11, 12])
    [17, 19, 21]
    """
    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """
    Subtracts two vectors of equal length together
    :param v: Vector v
    :param w: Vector w
    :return: Vector resulting from subtracting elements from each vector.
    >>> subtract([1, 2, 3], [4, 5, 6])
    [-3, -3, -3]
    >>> subtract([7, 8, 9], [1, 3, 5])
    [6, 5, 4]
    """
    # Check that both vectors are the same length
    assert len(v) == len(w), "Vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """
    This function will return the componentwise sum of a list of vectors
    :param vectors: A list of vectors
    :return: Componentwise sum of all vectors in the input list
    >>> vector_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [12, 15, 18]
    >>> vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]])
    [16, 20]
    """
    # Check that the input list is not empty
    assert vectors, "No vectors provided"

    # Check that all vectors are of the same length
    num_elem = len(vectors[0])
    assert all(len(v) == num_elem for v in vectors)

    # The ith element of the result is the sum of all ith elements in all vectros
    return [sum([vector[i] for vector in vectors]) for i in range(num_elem)]


def scalar_multiply(v: Vector, c: float) -> Vector:
    """
    Multiplies each element in Vector v but constant c
    :param v: Vector
    :param c: constant to multiply each elemnt by
    :return: resultant vector
    >>> scalar_multiply([1, 2, 3, 4, 5], 5)
    [5, 10, 15, 20, 25]
    >>> scalar_multiply([6, 7, 8, 9, 10], 3)
    [18, 21, 24, 27, 30]
    """
    return [i * c for i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """
    Computes the component wise mean of a list of vectors
    :param vectors: List of same length vectors
    :return: component wise mean of all vectors in list
    >>> vector_mean([[1, 2], [3, 4], [5, 6]])
    [3.0, 4.0]
    >>> vector_mean([[7, 8], [9, 10], [11, 12]])
    [9.0, 10.0]
    """
    n = len(vectors)
    return scalar_multiply(vector_sum(vectors), 1/n)


def dot(v: Vector, w: Vector) -> float:
    """
    The dot product is sum of all elements after a component wise multiplication of two vectors
    Computes v_1 * w_1 + ... + v_n * w_n
    :param v: First vector input
    :param w: Second vector input
    :return: returns the dot product of vector v and w
    >>> dot([1, 2, 3], [4, 5, 6])
    32
    """
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])


def sum_of_squares(v: Vector) -> float:
    """
    Computes the sum of all elements squared
    v_1 * v_1 + ... + v_n * v_n
    :param v: Input vector
    :return: sum of squares
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([4, 5, 6])
    77
    """
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """
    Computes the magnitude of a vector but taking the square root of the sum of squares
    :param v: Input Vector
    :return: square root of sum of squares
    >>> magnitude([1, 2, 3])
    3.7416573867739413
    >>> magnitude([4, 5, 6])
    8.774964387392123
    """
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """
    Computes (v_1 - v_2) ** 2 + ... + (v_n - v_n) ** 2
    :param v: First vector
    :param w: Second vector
    :return: returns the squared distance
    """
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """
    Computes the distance
    :param v: First vector
    :param w: Second vector
    :return: Distance
    """
    return math.sqrt(squared_distance(v, w))


if __name__ == '__main__':
    print(add([1, 2, 3], [4, 5, 6]))
    print(subtract([1, 2, 3], [4, 5, 6]))
    print(vector_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(scalar_multiply([1, 2, 3, 4, 5], 5))
    print(vector_mean([[7, 8], [9, 10], [11, 12]]))
    print(dot([1, 2, 3], [4, 5, 6]))
    print(sum_of_squares([4, 5, 6]))
    print(magnitude([4, 5, 6]))
