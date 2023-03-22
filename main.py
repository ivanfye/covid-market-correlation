"""CSC110 Fall 2021 Project: main

This python module, when run will load the necessary files from the datasets,
perform the computations on the data, and produce graphs.

This file is Copyright (c) 2021 Boaz Cheung, and Ivan Ye.
"""
import data_computing as dc
import data_reading as dr
import data_graphing as dg


countries = [('United States of America: S&P 500', dr.load_economy('index_sp500.csv'),
              dr.load_covid('covid_data_usa.csv'))]

# To look at Hong Kong, uncomment the lines below.
# To see all the graphs, do Not uncomment 'pop'

countries.append(('Hong Kong: Hang Seng Index', dr.load_economy('index_hangseng.csv'),
                  dr.load_covid('covid_data_hk.csv')))
# countries.pop(0)

for country in countries:
    percent_change = dc.calculate_percentage_change(country[1])
    daily_cases = dc.cases_per_day(country[2])
    daily_deaths = dc.deaths_per_day(country[2])
    daily = [(daily_cases, 'Cases'), (daily_deaths, 'Deaths')]

    for x in daily:
        points = dc.find_all_coordinates(percent_change, x[0])
        regress = dc.linear_regression(points)

        axis_num = dc.arr_axis(points)
        line = dc.slope_points(regress, axis_num)
        axis_slope = dc.arr_axis(line)

        dg.plot(axis_num, axis_slope, dc.find_correlation_coefficient(points),
                country[0], x[1])
