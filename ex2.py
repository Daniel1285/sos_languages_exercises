"""
Daniel Shalom cohen - 212991749
Natan Stern - 322879255
"""

from functools import reduce, wraps
from datetime import datetime, timedelta
import math
import time



def time_measure(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function - {func.__name__} - Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@time_measure
def imperative_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total #

@time_measure
def functional_sum(lst):
    return reduce(lambda a, b: a + b, lst)

@time_measure
def all_in_one():
    return sum(list(map(lambda x: 2 * x + 2, range(10000))))

@time_measure
def generate_dates(start_date_str, num_dates, day_skip):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    return list(map(lambda x: (start_date + timedelta(days=x * day_skip)).strftime("%d-%m-%Y"), range(num_dates)))

def power_function(exponent):
    return lambda base: base ** exponent

def power_functions_to(n):
    return map(lambda exponent: power_function(exponent), range(n))


def taylor_approximation(x, n):
    return sum([(func(x) / math.factorial(i)) for i,func in enumerate(power_functions_to(n+1))])


def task_manager():
    tasks = {}

    def add_task(task_name, status="incomplete"):
        tasks[task_name] = status

    def get_tasks():
        return tasks

    def complete_task(task_name):
        if task_name in tasks:
            tasks[task_name] = "complete"


    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }


def main():
# Question 1
    lst = list(map(lambda x: 2 * x + 2, range(10)))

    assert imperative_sum(lst) == 110, "imperative_sum failed"

    # Test for functional_sum
    assert functional_sum(lst) == 110, "functional_sum failed"

    # Test for all_in_one
    assert all_in_one() == 100010000, "all_in_one failed"

#Question 2
    numbers = list(range(1, 1000))

    even = [i for i in numbers if i%2 == 0]
    odd =  [i for i in numbers if i%2!=0]
    iter_odd = iter(odd[1:]) # No need for the first member
    y_even = [reduce(lambda a,b: a*b, even[:i]) for i in range(2,len(even)+1)]
    y_odd = list(map(lambda x:x/2+2+next(iter_odd), odd))

    print(f"y_even: {y_even}")
    print(f"y_odd = {y_odd}")
    print(f"sum of y_even = {sum(y_even)}")
    print(f"sum of y_odd = {sum(y_odd)}")




#Question 3
    # Test for generate_dates
    expected_dates = ["01-01-2024", "03-01-2024", "05-01-2024"]
    assert generate_dates("01-01-2024", 3, 2) == expected_dates, "generate_dates failed"

#Question 4
    # Test for power_function
    power_of_2 = power_function(2)
    assert power_of_2(3) == 9, "power_function(2) failed for base 3"
    assert power_of_2(5) == 25, "power_function(2) failed for base 5"

    #Test for power_functions_to
    powers = list(power_functions_to(3))
    for i , func in enumerate(powers):
        assert func(2) == pow(2,i), f"power_functions_to failed for exponent {i}"

    # Test for taylor_approximation (e^x approximation)
    approx = taylor_approximation(1, 5)  # e^1 approximation with 5 terms
    expected_value = sum([1 / math.factorial(i) for i in range(6)])  # e^1 = 1 + 1/1! + 1/2! + ... + 1/5!
    assert math.isclose(approx, expected_value, rel_tol=1e-4), "taylor_approximation failed for e^1"

#Question 5
    # Test for tasks_manager
    tasks_manager = task_manager()

    tasks_manager['add_task']("Write email")
    tasks_manager['add_task']("Shopping", "in progress")
    tasks_manager['add_task']("Homework")
    tasks = tasks_manager['get_tasks']()

    assert tasks == {
        "Write email": "incomplete",
        "Shopping": "in progress",
        "Homework": "incomplete"
    }, f"Test failed: {tasks}"


    tasks_manager['complete_task']("Write email")
    tasks = tasks_manager['get_tasks']()
    assert tasks["Write email"] == "complete", f"Test failed: {tasks}"
    assert tasks["Shopping"] == "in progress", f"Test failed: {tasks}"
    assert tasks["Homework"] == "incomplete", f"Test failed: {tasks}"

    print("All tests passed!")


if __name__ == "__main__":
    main()


