import pandas as pd
from pygal.style import DarkStyle
from datetime import datetime, timedelta
import pygal

bar_chart = pygal.Bar()
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.render_to_file('bar_chart.svg')

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]
chart = pygal.Line()
chart.force_uri_protocol = 'http'
chart.add('x^2', squares)
chart.render_to_file('squares.svg')

chart = pygal.Line()
chart.force_uri_protocol = 'http'
chart.title = "Squares"
chart.x_labels = x_values
chart.x_title = "Value"
chart.y_title = "Square of Value"
chart.add('x^2', squares)
chart.render_to_file('squares.svg')


date_chart = pygal.Line(x_label_rotation=20)
date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
    datetime(2013, 1, 2),
    datetime(2013, 1, 12),
    datetime(2013, 2, 2),
    datetime(2013, 2, 22)])
date_chart.add("Visits", [300, 412, 823, 672])
date_chart.render_in_browser()


# biar cakep
chart = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkStyle)
chart.add('A', [10, 30,  5, 16, 13, 3,  7])
chart.add('B', [25, 2,  3,  4,  5, 7, 12])
chart.add('C', [6, 10, 9,  7,  3, 15,  0])
chart.add('D', [2,  3, 5,  4, 12, 18,  5])
chart.add('E', [7,  4, 4,  1,  2, 25, 0])
chart.render_in_browser()


# pie chart
pie_chart = pygal.Pie()
pie_chart.title = 'Instrumentasi2020'
pie_chart.add('A', 20.5)
pie_chart.add('B', 36.0)
pie_chart.add('C', 35.9)
pie_chart.add('D', 5.5)
pie_chart.add('E', 1.3)
pie_chart.render_in_browser()
