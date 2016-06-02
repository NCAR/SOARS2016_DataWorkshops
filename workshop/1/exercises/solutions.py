import csv

# Write the Python script that opens that CSV file and emits the `month` and `day` columns.
def  print_columns(cols):
    with open("../data/sample_demo_weather_data_1981.csv") as f:
        csvFile = csv.DictReader(f)

        # print [for c in cols True if 'year' in csvFile.fieldnames else False]
        if all([c in csvFile.fieldnames for c in cols]):
            for l in csvFile:
                print ", ".join([l.get(c) for c in cols])


# Find the bounding box for the lat and lon data in the CSV file; that is, find the maximum and minumum longitude and latitude .  Your program should just emit 4 numbers. HINT: You may need to use the Python built-in function `float()` to properly do the calculations (see [Python docs about float](https://docs.python.org/2/library/functions.html#float)).
def get_bounding_box():
    with open("../data/sample_demo_weather_data_1981.csv") as f:
        csvFile = csv.DictReader(f)

        first_data = csvFile.next() # we have to intialize with something
        max_lat, min_lat, max_lon, min_lon = first_data['lat'], first_data['lat'], first_data['lon'], first_data['lon']
        
        for l in csvFile:
            lat, lon = l['lat'], l['lon']

            if lat > max_lat:
                max_lat = lat

            if lat < min_lat:
                min_lat = lat

            if lon > max_lon:
                max_lon = lon

            if lon < min_lon:
                min_lon = lon

        print max_lat, min_lat, max_lon, min_lon


# Find out the frequency of measurements by month -- that is how many data points do we have by month?  HINT: A dictionary will be your friend.  Your program should emit something like this:
def get_frequency(col='month'):
    freq_dict = {}

    with open("../data/sample_demo_weather_data_1981.csv") as f:
        csvFile = csv.DictReader(f)

        for l in csvFile:
            month = int(l['month'])

            if month in freq_dict:
                freq_dict[month] += 1
            else:
                freq_dict[month] = 1

            #
            # TRY THIS IDIOM :
            # freq_dict[month] = freq_dict.get(month,0) + 1
            #

    # a little nicety of Python, import when you need
    import pprint
    pprint.PrettyPrinter(indent=1).pprint(freq_dict)


''''
"Bad" data is all around us ... for now let's define "bad" as data that seems
unusually outside the average of the data we have.  Because the
file is so small, we might be able to do this by eyeballing it, but instead,
write the program that finds "bad" data.  HINT: You can use any mechanism you'd
like, but Python has a few built-in goodies you may want to try --

[len()](https://docs.python.org/2.7/library/functions.html#len),
[sum()](https://docs.python.org/2.7/library/functions.html#sum),
[max()](https://docs.python.org/2.7/library/functions.html#max) and
[min()](https://docs.python.org/2.7/library/functions.html#sum) are clues.

'''
def find_bad_data(col='raintot', cast=float, min=0, max=999):
    with open("../data/sample_demo_weather_data_1981.csv") as f:
        csvFile = csv.DictReader(f)

        for l in csvFile:
            data = cast(l[col])
            if data < min or data > max:
                print "Bad data [col='{}', min={}, max={}] : {}".format(col, min, max, data)

        # how would we get the associated row number?
        # how can we improve this so we do not need to pass in parameters?
        # why might we do it that way?


if __name__ == "__main__":

    # 1_print_columns(['month', 'day'])
    # 2_get_bounding_box()
    # 3_get_frequency()
    # 4_find_bad_data('tmaxavg')

    pass