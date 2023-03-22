"""CSC110 Fall 2021 Project: Data Calculations

This python module contains all the functions that make calculations in
this project.

This file is Copyright (c) 2021 Boaz Cheung, and Ivan Ye.
"""
import datetime
import math
from data_reading import Covid, Economy


def find_all_coordinates(eco_data: list[(datetime, float)], covid_data: list[tuple]) -> list[tuple]:
    """Returns a list of all the points, represented as (x, y)

    Preconditions:
        - eco_data != []
        - covid_data != []
    """
    coord = []
    for eco in eco_data:
        for covid in covid_data:
            if eco[0] == covid[0]:
                coord.append((covid[1], eco[1]))
    return coord


def slope_points(linear: tuple[float, float], axis: tuple[list, list]) -> list[tuple]:
    """Returns a list of the points of the slope

    Preconditions:
        - linear != ()
        - axis != ()

    >>> ax = ([4, 2, 5, 125], [2, 234, 12, 1])
    >>> slope_points((6.166666666666667, -0.25), ax)
    [(0, 6.166666666666667), (125, -25.083333333333332)]
    """
    initial = (0, linear[0])
    points = [initial]
    inc = max(axis[0])

    po = (points[-1][0] + inc, points[-1][1] + linear[1] * inc)
    points.append(po)

    return points


def arr_axis(points: list[tuple]) -> tuple[list, list]:
    """Return a tuple that contains the list of the x and y-coordinates respectively

    Preconditions:
        - points != ''

    >>> pts = [(2,4), (6,8), (10, 2)]
    >>> arr_axis(pts)
    ([2, 6, 10], [4, 8, 2])
    """
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])
    return (x, y)


def linear_regression(data: list[tuple]) -> tuple[float, float]:
    """Returns a tuple of the y-intercept and the slope of the linear regression
    of a data set, represented as (y-intercept, slope)

    Preconditions:
        - data != []

    >>> points = [(2,4), (6,8), (10, 2)]
    >>> linear_regression(points)
    (6.166666666666667, -0.25)
    """
    total = summation(data)
    y = (total['sum_y'] * total['sum_x_sq'] - total['sum_x'] * total['sum_xy']) \
        / (total['n'] * total['sum_x_sq'] - total['sum_x'] ** 2)
    slope = (total['n'] * total['sum_xy'] - total['sum_x'] * total['sum_y']) \
        / (total['n'] * total['sum_x_sq'] - total['sum_x'] ** 2)

    return (y, slope)


def find_correlation_coefficient(data: list[tuple]) -> float:
    """Return the correlation coefficient

    Preconditions:
        - data != []

    >>> points = [(2,4), (6,8), (10, 2)]
    >>> find_correlation_coefficient(points)
    -0.32733
    """
    total = summation(data)
    ans = ((total['n'] * total['sum_xy']) - (total['sum_x'] * total['sum_y'])) \
        / math.sqrt((total['n'] * total['sum_x_sq'] - total['sum_x'] ** 2)
                    * (total['n'] * total['sum_y_sq'] - total['sum_y'] ** 2))

    return round(ans, 5)


def summation(data: list[tuple]) -> dict:
    """Return a dict of the sum of the x, y values in its various forms

    Preconditions:
        - data != []

    >>> points = [(2,4), (6,8), (10, 2)]
    >>> summation(points)
    {'sum_xy': 76, 'sum_x': 18, 'sum_y': 14, 'sum_x_sq': 140, 'sum_y_sq': 84, 'n': 3}
    """
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sq = 0
    sum_y_sq = 0
    n = len(data)
    list_x_sq = []
    list_y_sq = []
    d = {}

    for value in data:
        sum_x += value[0]
        sum_y += value[1]
        sum_xy += (value[0] * value[1])
        list_x_sq.append(value[0] ** 2)
        list_y_sq.append(value[1] ** 2)

    for x in list_x_sq:
        sum_x_sq += x

    for y in list_y_sq:
        sum_y_sq += y

    d['sum_xy'] = sum_xy
    d['sum_x'] = sum_x
    d['sum_y'] = sum_y
    d['sum_x_sq'] = sum_x_sq
    d['sum_y_sq'] = sum_y_sq
    d['n'] = n
    return d


def cases_per_day(total: list[Covid]) -> list[tuple]:
    """Return a list of tuples that contain the date and the number of cases on that date

    Preconditions:
        - total != []

    >>> cases = [Covid(date=datetime.date(2020, 1, 22), cases=2, deaths=0, hospital_critical=0),\
    Covid(date=datetime.date(2020, 1, 23), cases=10, deaths=0, hospital_critical=0)]
    >>> cases_per_day(cases)
    [(datetime.date(2020, 1, 22), 2), (datetime.date(2020, 1, 23), 8)]
    """
    total_cases = []
    prev = 0
    for c in total:
        new = c.cases - prev
        prev = c.cases
        per_day = (c.date, new)
        total_cases.append(per_day)

    return total_cases


def deaths_per_day(total: list[Covid]) -> list[tuple]:
    """Returns a list of tuples that contain the date and the number of deaths on that date

    Preconditions:
        - total != []

    >>> deaths = [Covid(date=datetime.date(2020, 1, 22), cases=2, deaths=3, hospital_critical=0),\
    Covid(date=datetime.date(2020, 1, 23), cases=10, deaths=12, hospital_critical=0)]
    >>> deaths_per_day(deaths)
    [(datetime.date(2020, 1, 22), 3), (datetime.date(2020, 1, 23), 9)]
    """
    total_deaths = []
    prev = 0
    for d in total:
        new = d.deaths - prev
        prev = d.deaths
        per_day = (d.date, new)
        total_deaths.append(per_day)

    return total_deaths


def calculate_percentage_change(data: list[Economy]) -> list[tuple[datetime, float]]:
    """Returns a list of tuples that contain the date and the number of covid cases on that date

    Preconditions:
        - total != []

    >>> economy = [Economy(date=datetime.date(2020, 1, 13), close=3288.13), \
    Economy(date=datetime.date(2020, 1, 14), close=3283.15)]
    >>> calculate_percentage_change(economy)
    [(datetime.date(2020, 1, 14), -0.1514538658751332)]
    """
    change = []
    for day in range(1, len(data)):
        change.append((data[day].date, 100 * (data[day].close - data[day - 1].close)
                       / data[day - 1].close))
    return change


if __name__ == '__main__':
    import doctest
    import python_ta
    import python_ta.contracts

    doctest.testmod(verbose=True)
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'math', 'datetime', 'data_reading'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
