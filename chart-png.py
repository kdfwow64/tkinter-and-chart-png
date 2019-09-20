import matplotlib
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
import babel.numbers
import decimal

matplotlib.use('TkAgg')


def dollar(x, pos):
    'The two args are the value and tick position'
    return x

def csv_to_png(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        chart_type = 0
        x = []
        y = []
        format_str = "%m/%d/%Y"
        for row in csv_reader:
            if line_count == 0:
                if row[0] == 'date':
                    chart_type = 0
                else:
                    chart_type = 1
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if chart_type == 0:
                    y.append(row[1])
                    datetime_obj = datetime.datetime.strptime(row[0], format_str)
                    x.append(datetime_obj)
                else:
                    x.append(row[0])
                    y.append(row[1])
                line_count += 1
        line_count -= 1
        if chart_type == 0:
            plt.figure()
            plt.plot(x, y)
            new_y = []
            y_label = []

            for i in range(1, line_count):
                if i % 6 == 5:
                    # ss = '$d' + '{:20,.2f}'.format(float(y[i]))
                    ss = babel.numbers.format_currency(decimal.Decimal(y[i]), "USD")
                    new_y.append(y[i])
                    y_label.append(ss)
            plt.yticks(new_y)
            plt.xticks(x)
            cur_axes = plt.gca()
            # cur_axes.axes.get_xaxis().set_visible(False)
            cur_axes.axes.get_xaxis().set_ticklabels([])

            cur_axes.tick_params(direction='in', length=6, width=1, colors='black',
                           grid_color='black', grid_alpha=0.5)
            plt.title("Historical Performance")
            plt.gcf().autofmt_xdate()


            cur_axes.set_yticklabels(y_label)

            plt.show()

        else:
            fig, ax = plt.subplots()

            size = 0.3

            cmap = plt.get_cmap("tab20c")
            outer_colors = cmap(np.arange(line_count) * line_count)

            ax.pie(y, labels=x, radius=1, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))
            ax.set(aspect="equal", title='Chart Title')
            plt.show()
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scan-path", help="path of csv")

    args = parser.parse_args()

    if os.path.isfile(args.scan_path):
        csv_to_png(args.scan_path)
    else:
        print("Can not find the csv file from {}".format(args.scan_path))
