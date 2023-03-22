"""CSC110 Fall 2021 Project: Data Reader

This python module contains the data classes and their loading functions for
the project.

This file is Copyright (c) 2021 Boaz Cheung, and Ivan Ye.
"""
import datetime
import csv
from dataclasses import dataclass


@dataclass
class Economy:
    """The closing prices of the index fund on a day

    Instance Attributes:
        - date: the date
        - close: the closing price

    Representation Invariants:
        - self.close > 0
        - 2020 <= self.date.year <= 2021
        - 1 <= self.date.month <= 12
        - 1 <= self.date.day <= 31
    """
    date: datetime.date
    close: float


@dataclass
class Covid:
    """Information in regards to covid on a day

    Instance Attributes:
        - date: the date
        - cases: the total amount of positive cases
        - deaths: the total amount of deaths
        - hospital_critical: the amount of critical hospitalizations

    Representation Invariants:
        - self.cases >= 0
        - self.deaths >= 0
        - self.hospital_critical >= 0
        - 2020 <= self.date.year <= 2021
        - 1 <= self.date.month <= 12
        - 1 <= self.date.day <= 31
    """
    date: datetime.date
    cases: int
    deaths: int
    hospital_critical: int


def load_economy(filename: str) -> list[Economy]:
    """Return a list containing Economy based on the data in filename.

    The data in filename is in a csv format with 2 columns. Those being date and closing
    prices, in that order.
    """
    economy = []

    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            day = row[0].split(' ')
            day = day[0].split('/')
            day = datetime.date(int(day[2]), int(day[0]), int(day[1]))
            economy.append(Economy(day, float(row[1])))

    return economy


def load_covid(filename: str) -> list[Covid]:
    """Return a list containing Covid based on the data in filename.

    The data in filename is in a csv format with 4 columns. Those being date, cases,
    deaths, and hospitalized, in that order.
    """
    cases = []

    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)  # skip the header

        for row in reader:
            day = row[0].split('/')
            day = datetime.date(int(day[2]), int(day[1]), int(day[0]))
            cases.append(Covid(day, int(row[1]), int(row[2]), int(row[3])))

    return cases


if __name__ == '__main__':
    import doctest
    import python_ta
    import python_ta.contracts

    doctest.testmod(verbose=True)
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'csv', 'datetime', 'dataclasses'],
        'allowed-io': ['load_covid', 'load_economy'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
