from anniversary_generator import anniversaries

from datetime import datetime, timedelta

YEARS_PAST = 5
MAX_AGE = 100
FORMAT = "%b. %d, %Y"

while True:
    try:
        string = input("Enter your birthday (1987-8-5): ")
        if not string:
            year, month, day = 1987, 8, 5
        else:
            year, month, day = [int(s) for s in string.split("-")]
        birthday = datetime(year, month, day)
        print()
        now = datetime.now()
        year_ago = now - timedelta(days=365 * YEARS_PAST)
        really_old = birthday + timedelta(days=365 * MAX_AGE)
        generator = anniversaries(birthday, really_old)
        anns = [ann for ann in generator if ann.time > year_ago]
        anns = sorted(anns, key=lambda ann: ann.time)
        for ann in anns:
            if ann.time < now:
                print("On %s you were %s %s old." % (
                    ann.time.strftime(FORMAT),
                    ann.number.display_value,
                    ann.units,
                ))
            else:
                print("On %s you will be %s %s old." % (
                    ann.time.strftime(FORMAT),
                    ann.number.display_value,
                    ann.units,
                ))
        print()
    except ValueError as e:
        print("Invalid input!")
