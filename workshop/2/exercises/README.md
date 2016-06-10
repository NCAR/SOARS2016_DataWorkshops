# Supplemental Exercises

There is a file in `/data` called [sample_demo_weather_data_1981.csv](../data/sample_demo_weather_data_1981.csv).  All the exercises below should be performed on that file

In the last workshop's exercises, we talked about manually finding bounding boxes and frequency distributions.  Now that you know something about Pandas, try the following:

* Find the bounding box for the lat and lon data in the CSV file using Pandas.
* Find out the frequency of measurements by month -- that is how many data points do we have by month?
* Which months are suspect in terms of their measurement counts?
* Plot the temperature data and determine of there are any anomolies that you can visually detect.
* For a given month, create a dataframe that includes the monthly  and quarterly raintotal averages.  Your dataframe should look something like :

| month | day | year | raintot | monthavg | seasonavg |
|-------|-----|------|---------|----------|-----------|
| 1     | 1   | 1981 | 12      | 8.34     |  7.18     |

Hint: Don't forget Dataframes can be concatenated with `+`.