"""
Daniel Shalom cohen - 212991749
Natan Stern - 322879255
"""


# Question 1
def getPentaNum(n):
    return n * (3 * n - 1) // 2


def pentaNumRange(n1, n2):
    return [getPentaNum(i) for i in range(n1, n2)]


# Question 2
def sumDigit(n):
    return sum(int(number) for number in str(n))


# Question 3
def gematriaVal(str_key):
    g = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20,
         'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
         }
    return sum([g[i] for i in str_key])


# Question 4
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def twinPrimes(n):
    return [(i, n) for i in range(n - 2, n + 3) if isPrime(i) and isPrime(n) and i!=n]


def allTwinPrime(n):
    return {i: twinPrimes(i) for i in range(2, n + 1) if isPrime(i)}


# Question 6
def multiply_by_2(x):
    return x * 2


def square(x):
    return x ** 2


def inverse(x):
    return 1 / x if x != 0 else None


def apply_functions(numbers, functions):
    return {func.__name__: [func(j) for j in numbers] for func in functions}


def main():

    assert getPentaNum(1) == 1
    assert getPentaNum(2) == 5
    assert getPentaNum(3) == 12
    assert getPentaNum(4) == 22

    # Test pentaNumRange
    assert pentaNumRange(1, 5) == [1, 5, 12, 22]
    assert pentaNumRange(2, 4) == [5, 12]

    # Test sumDigit
    assert sumDigit(123) == 6
    assert sumDigit(98765) == 35

    # Test gematriaVal
    assert gematriaVal('אב') == 3
    assert gematriaVal('שבת') == 702

    # Test isPrime
    assert isPrime(2) is True
    assert isPrime(4) is False
    assert isPrime(13) is True
    assert isPrime(20) is False

    # Test twinPrimes
    assert twinPrimes(5) == [(3, 5), (7, 5)]
    assert twinPrimes(11) == [(13, 11)]
    assert twinPrimes(8) == []

    # Test allTwinPrime
    assert allTwinPrime(11) == {2: [(3, 2)], 3: [(2, 3), (5, 3)], 5: [(3, 5), (7, 5)], 7: [(5, 7)], 11: [(13, 11)]}


    # Test apply_functions
    numbers = [1, 2, 3]
    functions = [multiply_by_2, square, inverse]
    result = apply_functions(numbers, functions)
    assert result['multiply_by_2'] == [2, 4, 6]
    assert result['square'] == [1, 4, 9]
    assert result['inverse'] == [1.0, 0.5, 0.3333333333333333]

    print("All tests passed!")


if __name__ == '__main__':
    main()
