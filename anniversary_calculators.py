from datetime import datetime, timedelta

from anniversary import Anniversary

# Each function represents some unit of time.
# It takes a base_time and a Number,
# creates a new time by adding number.value units to base_time,
# and returns an Anniversary.

# (The list of all calculators is declared at the bottom of this file.)

def seconds(base_time, number):
    time = base_time + timedelta(seconds=number.value)
    return Anniversary(
        base_time=base_time,
        time=time,
        units="seconds",
        number=number,
    )
    
def minutes(base_time, number):
    time = base_time + timedelta(minutes=number.value)
    return Anniversary(
        base_time=base_time,
        time=time,
        units="minutes",
        number=number,
    )
    
def hours(base_time, number):
    time = base_time + timedelta(hours=number.value)
    return Anniversary(
        base_time=base_time,
        time=time,
        units="hours",
        number=number,
    )
    
def days(base_time, number):
    time = base_time + timedelta(days=number.value)
    return Anniversary(
        base_time=base_time,
        time=time,
        units="days",
        number=number,
    )
    
def weeks(base_time, number):
    time = base_time + timedelta(weeks=number.value)
    return Anniversary(
        base_time=base_time,
        time=time,
        units="weeks",
        number=number,
    )
    
def years(base_time, number):
    # TODO: is this the right way to handle leap day?
    year = base_time.year + number.value
    try:
        time = base_time.replace(year=year)
    except ValueError as error:
        if base_time.month == 2 and base_time.day == 29:
            time = base_time.replace(
                month=2,
                day=28,
                year=year,
            )
        else:
            raise error
    return Anniversary(
        base_time=base_time,
        time=time,
        units="years",
        number=number,
    )
    
CALCULATORS = [
    seconds,
    minutes,
    hours,
    days,
    weeks,
    years,
]
