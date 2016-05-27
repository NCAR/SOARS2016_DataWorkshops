# Supplemental Exercises

There is a file in `/data` called [sample_demo_weather_data_1981.csv](../data/samepl_demo_weather_data_1981.csv).  All the exercises below should be performed on that file

For fun do the follow :

* Write the Python script that opens that CSV file and emits the `month` and `day` columns.
* Find the bounding box for the lat and lon data in the CSV file; that is, find the maximum and minumum longitude and latitude .  Your program should just emit 4 numbers. HINT: You may need to use the Python built-in function `float()` to properly do the calculations (see [Python docs about float](https://docs.python.org/2/library/functions.html#float)).
* Find out the frequency of measurements by month -- that is how many data points do we have by month?  HINT: A dictionary will be your friend.  Your program should emit something like this:


        Jan : 5 total measurements
        Feb : 54 total measurements
        ...
* Run the following code in PyCharm:

        import pprint

        simple_dictionary = dict(jan=5, feb=50, mar=500)
        pprint.PrettyPrinter(indent=5).pprint(simple_dictionary)


* "Bad" data is all around us ... for now let's define "bad" as data that seems unusually outside the average of the data we have.  Because the file is so small, we might be able to do this by eyeballing it, but instead, write the program that finds "bad" data.  HINT: You can use any mechanism you'd like, but Python has a few built-in goodies you may want to try -- [len()](https://docs.python.org/2.7/library/functions.html#len), [sum()](https://docs.python.org/2.7/library/functions.html#sum), [max()](https://docs.python.org/2.7/library/functions.html#max) and [min()](https://docs.python.org/2.7/library/functions.html#sum) are clues.
