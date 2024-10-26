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


def sortedzip(lists):
    if all(not lst for lst in lists):
        return []

    sorted_lists = [sorted(lst) for lst in lists]
    first_elements = tuple(lst[0] for lst in sorted_lists)

    return [first_elements] + sortedzip([lst[1:] for lst in sorted_lists])

@time_measure
def sorted_zip_tail(l):
    def helper(l):
        return [] if not l else [sorted(l[0])] + helper(l[1:])
    return zip(*helper(l))

@time_measure
def create_simple_array():
    return list(range(10001))
start_time = time.time()
arr = create_simple_array()
print(f" Time: {time.time() - start_time}")
print(f"Size : {sys.getsizeof(arr)}")
print(f" Type: {type(arr)}")

@time_measure
def create_lazy_array():
    return (i for i in range(10001))
start_time = time.time()

lazy_arr = create_lazy_array()
print(f" Time: {time.time() - start_time}")
print(f"Size : {sys.getsizeof(lazy_arr)}")
print(f"Type: {type(lazy_arr)}")

@time_measure
def create_half_lazy_array(lazy_arrey):
    return (x for x in lazy_arr)

start_time = time.time()
half_lazy = create_half_lazy_array(create_lazy_array())
print(f" Time: {time.time() - start_time}")
print(f"Size : {sys.getsizeof(half_lazy)}")
print(f"Type: {type(lazy_arr)}")


@time_measure
def create_half_simple_array(lazy_array):
    return lazy_array[:5001]
start_time = time.time()
arr = create_half_simple_array(create_simple_array())
print(f" Time: {time.time() - start_time}")
print(f"Size : {sys.getsizeof(arr)}")
print(f" Type: {type(arr)}")

def prime_generator():
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
gen = prime_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


from math import factorial

def taylor_series(x):
    k = 0
    current_sum = 0
    while True:
        term = (x ** k) / (factorial(k) if k > 0 else 1)
        current_sum += term
        yield current_sum
        k += 1

taylor_gen = taylor_series(2)
print(next(taylor_gen))
print(next(taylor_gen))
print(next(taylor_gen))
print(next(taylor_gen))
print(next(taylor_gen))

def main():
    print(list(sortedzip([[3,1,2],[5,6,4],['a','b','c']])))
    print(list(sorted_zip_tail([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))
    #1
    print(tuple_recursive(100))
    print(tuple_tail_recursive(100))
    #2
    print(sum_recursive(tuple_recursive(100)))
    print(sum__tail_recursive(tuple_tail_recursive(100)))
    #4
    print(is_palindrome_recursive(123454321))
    print(is_palindrome_tail_recursive(123454321))
    #5
    print(list(sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))
    print(list(sorted_zip_tail([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))



if __name__ == "__main__":
    main()

