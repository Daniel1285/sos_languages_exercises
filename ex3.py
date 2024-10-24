"""
Daniel Shalom cohen - 212991749
Natan Stern - 322879255
"""

import time
import sys
import math

from functools import  wraps


sys.setrecursionlimit(2000)  # Increase the recursion limit

def time_measure(func):
    func._in_recursion = False

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not func._in_recursion:
            start_time = time.perf_counter()
            func._in_recursion = True
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Total time for -{func.__name__}-: {total_time:.4f} seconds")
            print(f"Memory size: {sys.getsizeof(result)} bytes")
            func._in_recursion = False
            return result
        else:
            return func(*args, **kwargs)

    return wrapper

@time_measure
def tuple_recursive(n = 1000):
    return () if n == 0 else (n,) + tuple_recursive(n-1)

@time_measure
def tuple_tail_recursive(n=1000, t=()):
    return t if n == 0 else tuple_tail_recursive(n-1, (n,) + t)

@time_measure
def sum_recursive(t):
    return 0 if t == () else t[0] + sum_recursive(t[1:])

@time_measure
def sum__tail_recursive(t, result=0):
    return result if t == () else sum__tail_recursive(t[1:], result+t[0])


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

@time_measure
def is_palindrome_recursive(num):
    num = str(num)
    if len(str(num)) <=1:
        return True
    return False if num[0] != num[-1] else is_palindrome_recursive(num[1:-1])

@time_measure
def is_palindrome_tail_recursive(num):
    def helper(s, start, end):
        if start == end:
            return True
        if s[start] != s[end]:
            return False
        return helper(s, start + 1, end - 1)


    return helper(str(num), 0, len(str(num)) - 1)

#TODO
def sortedzip(l):
    return [] if not l else zip(*list(sorted(i) for i in l))


@time_measure
def sorted_zip_tail(l):
    def helper(l):
        return [] if not l else [sorted(l[0])] + helper(l[1:])
    return zip(*helper(l))

@time_measure
def create_simple_array():
    return [i for i in range(1000001)]

@time_measure
def create_lazy_array():
    return (i for i in range(1000001))


@time_measure
def create_half_lazy_array(lazy_array):
    return (next(lazy_array) for _ in range(5000))

@time_measure
def create_half_simple_array(lazy_array):
    return lazy_array[:5000]


def main():
    n = 999
    print(list(sortedzip([[3,1,2],[5,6,4],['a','b','c']])))
    assert tuple_recursive(n-1) == tuple(range(1, n).__reversed__()), f"tuple_Recursion failed!"
    assert tuple_tail_recursive(n-1) == tuple(range(1, n)), f"tuple_tail_recursive failed!"

    t = tuple_recursive(n-1)
    sum_t = sum_recursive(t)
    sum_tail = sum__tail_recursive(t)
    assert sum_t == sum(t), f"Got {sum_t} instead of {sum(t)}"
    assert sum_tail == sum(t), f"Got {sum_tail} instead of {sum(t)}"

    result = lcm(6,4)
    assert result == 12, f"Got {result} instead of 12"

    assert is_palindrome_recursive(123454321) == True, "not Palindrome"
    assert is_palindrome_tail_recursive(123454321) == True, "not Palindrome"

    l = [[3,1,2],[5,6,4],['a','b','c']]

    sort_zip = list(sortedzip(l))
    sort_zip_tail = list(sorted_zip_tail(l))
    print(sort_zip_tail)
    sort_zip_expected =  list(zip(*map(sorted,l)))
    assert sort_zip == sort_zip_expected, f"Got: {sort_zip} instead of {sort_zip_expected}"
    assert sort_zip_tail == sort_zip_expected, f"Got: {sort_zip} instead of {sort_zip_expected}"
    print("#################### Part 2 ####################")

    simple_array = create_simple_array()
    half_simle = create_half_simple_array(simple_array)
    lazy_array = create_lazy_array()
    half_lazy = create_half_lazy_array(lazy_array)


if __name__ == "__main__":
    main()

