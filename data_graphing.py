"""CSC110 Fall 2021 Project: Data Grapher

This python module contains the graphing function.

This file is Copyright (c) 2021 Boaz Cheung, and Ivan Ye.
"""
import matplotlib.pyplot as plt


def plot(axis_points: tuple[list, list], line: tuple[list, list], correlation: float,
         country: str, cd: str) -> None:
    """Plot a scatter-plot using the given points and a line of best fit on top.

    Preconditions:
        - axis_points != ()
        - line != ()
        - -1 <= correlation <= 1
        - country != ''
        - cd in {'Cases', 'Deaths'}
    """
    plt.style.use('seaborn-dark')
    plt.figure(figsize=(11, 6))
    plt.scatter(axis_points[0], axis_points[1], c='purple')
    plt.plot(line[0], line[1], c='blue')

    plt.xlabel('Covid ' + cd + ' per Day')
    plt.ylabel('% Change of Index')
    plt.title('Relationship Between the % Change of Index and Covid ' + cd
              + ' per Day from Jan 2020 to Mar 2021')

    plt.figtext(.6, .2, 'Correlation Coefficient: ' + str(correlation))
    plt.figtext(.45, .84, country)
    plt.show()


if __name__ == '__main__':
    import doctest
    import python_ta
    import python_ta.contracts

    doctest.testmod(verbose=True)
    python_ta.contracts.check_all_contracts()

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'matplotlib.pyplot'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
