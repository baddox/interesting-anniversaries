from itertools import count
from math import floor

from number import Number

# Each function is a generator that yields a (probably infinite) increasing
# sequence of numerical values (probably integers) that are "interesting" for
# some reason (described in the category field).

# (The list of all generators is declared at the bottom of this file.)

def powers_of_ten():
    for exponent in count():
        value = 10 ** exponent
        with_commas = "{:,}".format(value)
        yield Number(
            value=value,
            display_value=with_commas,
            formatted_value=with_commas,
            category="powers of ten",
        )

def powers_of_two():
    # Start at 2^2=4 because 2^0=1 and 2^1=2 aren't interesting.
    for exponent in count(2):
        value = 2 ** exponent
        with_commas = "{:,}".format(value)
        yield Number(
            value=value,
            display_value="2^%s" % exponent,
            formatted_value=with_commas,
            category="powers of two",
        )
        
def factors_of_ten():
    # 2, 5, 20, 50, 200, 500, ... 2,000,000, 5,000,000, ...
    factors = (2, 5)
    for exponent in count():
        power_of_ten = 10 ** exponent
        for factor in factors:
            value = factor * power_of_ten
            with_commas = "{:,}".format(value)
            yield Number(
                value=value,
                display_value=with_commas,
                formatted_value=with_commas,
                category="factors of ten"
            )

def repeated_digits():
    # https://oeis.org/A010785
    # Numbers with a single digit repeated.
    # 1, 2, 3, ... 11, 22, 33, 44, 55, 66, 77, 88, 99, ...
    # 111, 222, 333, ... 1111, 2222, 3333, ...
    digits = range(1, 10)
    # Start at 3-digit numbers, since 11, 22, etc. aren't very interesting.
    for exponent in count(3):
        power_of_ten = 10 ** exponent
        # https://oeis.org/A002275
        all_ones = (power_of_ten - 1) // 9
        for digit in digits:
            value = digit * all_ones
            with_commas = "{:,}".format(value)
            yield Number(
                value=value,
                display_value=with_commas,
                formatted_value=with_commas,
                category="repeated digits",
            )

def counting_up():
    # https://oeis.org/A057137
    # 1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789,
    # 1234567890, 12345678901, 123456789012, ...
    # Start at 5 digits (12345)
    for x in count(5):
        power_of_ten = 10 ** x
        # Magic from OEIS
        value = floor((137174210 / 1111111111) * power_of_ten)
        with_commas = "{:,}".format(value)
        yield Number(
            value=value,
            display_value=with_commas,
            formatted_value=with_commas,
            category="ascending digits",
        )

GENERATORS = [
    powers_of_ten,
    powers_of_two,
    factors_of_ten,
    repeated_digits,
    counting_up,
]
