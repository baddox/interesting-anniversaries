from itertools import product

from number_generators import GENERATORS
from anniversary_calculators import CALCULATORS

# Takes a base_time and generates an unsorted sequence of anniversaries from
# that base_time. All anniversaries < max_time will be generated.
def anniversaries(base_time, max_time):
    for generator, calculator in product(GENERATORS, CALCULATORS):
        for number in generator():
            try:
                anniversary = calculator(base_time, number)
            except ValueError:
                # When the time gets out of range for the Time class.
                break
            if anniversary.time > max_time:
                break
            yield anniversary

# TODO: is there a way to make `anniversaries` an infinite generator, but allow
# another function to skip to the next generator when exceeding a max_time?
# Does that idea even make sense?
