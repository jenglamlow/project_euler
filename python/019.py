# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime


# Using datetime library
def answer():
    d0 = datetime.date(1901, 1, 1)
    d1 = datetime.date(2000, 12, 31)

    count = 0

    while d0 <= d1:
        if (d0.weekday() == 6):
            count+=1
        d0 = d0 + datetime.timedelta(days=32)
        d0 = d0.replace(day=1)

    return count

# print(answer())


# Without using datetime library
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def answer2():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    sun = 0
    day = 1

    for year in range(1900, 2001):
        if is_leap_year(year):
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28
        for days in days_in_month:
            if day == 0 and year != 1900:
                sun += 1
            day = 6 - (days - day) % 7

    return sun

print(answer2())