import csv
import matplotlib.pyplot as plt 
from datetime import datetime

# save data to filename variable, page 347
# source: https://codinginfinite.com/data-visualizing-csv-format-chart-using-python-matplotlib/
filename = 'data/sitka_weather_2018_full.csv'

# use open function to save the contents of filename to var f
with open(filename) as f:

    # csv.reader scans f, header_row will find the first line of the file
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get high temperatures from the file, and dates too, and lows 
    dates, highs, lows = [], [], []

    # region this is reader method 1 to avoid errors!

    # for row in reader: 
    #     current_date = datetime.strptime(row[2], '%Y-%m-%d')
    #     high = row[8] # get values from row 8, high temps in file
    #     low = row[9]
    #     dates.append(current_date)
    #     highs.append(high)
    #     lows.append(low)
    #     highs[:] = [x for x in highs if x] # remove empty spots from list
    #     inthighs = [int(x) for x in highs] # convert each items in highs to an int
    #     lows[:] = [x for x in lows if x]
    #     intlows = [int(x) for x in lows]
    
    #endregion

    # region this is reader method 2 to avoid errors
    for row in reader: 
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[8]) # get values from row 8, high temps in file
            low = int(row[9])
        except ValueError:
            print(f"Missing Data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # endregion

    # for debugging purposes, use inthighs and intlows when using reader method 1
    # print(highs)
    # print(lows)
    # print(dates)

    # plot the high temperatures, swap 'highs' and 'lows' for
    # 'inthighs' and 'intlows' if using reader method 1
    plt.style.use('seaborn')
    fig, ax, = plt.subplots()
    ax.plot(dates, highs, c='red', alpha = 0.5) # plot high temps vs dates, alpha is alpha albedo
    ax.plot(dates, lows, c = 'blue', alpha = 0.5) # plot low temps vs dates
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1) # shade area between plot lines

    # format plot
    plt.title('Daily high and low temps, Jan 1st 2018 to Dec 31st 2018', fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

    plt.show()