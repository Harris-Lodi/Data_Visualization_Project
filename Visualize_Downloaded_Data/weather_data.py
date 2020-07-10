import csv
import matplotlib.pyplot as plt 
from datetime import datetime

# save data to filename variable, page 340
# source: https://codinginfinite.com/data-visualizing-csv-format-chart-using-python-matplotlib/
filename = 'data/sitka_weather_2018_full.csv'

# use open function to save the contents of filename to var f
with open(filename) as f:

    # csv.reader scans f, header_row will find the first line of the file
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get high temperatures from the file, and dates too
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = row[8] # get values from row 8, high temps in file
        dates.append(current_date)
        highs.append(high)
        highs[:] = [x for x in highs if x] # remove empty spots from list
        inthighs = [int(x) for x in highs] # convert each items in highs to an int

    # print(inthighs)
    # print(dates)

    # plot the high temperatures
    plt.style.use('seaborn')
    fig, ax, = plt.subplots()
    ax.plot(dates, inthighs, c='red')

    # format plot
    plt.title('Daily high temps, Jan 1st 2018 to Dec 31st 2018', fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()