# Text Files

Files in Python are exceedingly easy to work with.  There are a few things to remember when we get started:

* the "end of line" is a newline (return),
* the "end of file" is handled for you, so you don't have to worry about checking in the general case,
* try initially to think about a text file as a list of lines, where each line is the next entry in the list.

## Loading a file
A file can be loaded by the absolute or relative path to your executing program.  We'll keep things simple for now and run everything relative.

Say we have a file of numbers, where there are *two* numbers per line, each separated by a tab (whitespace).  Let's first pretend we have a list of such numbers:

    lst_of_number_strings = ["123.8    -38.79", "123.95    -39.75", "123.99    -36.79"]
    for s in lst_of_number_strings:
        print s

We should get:

    123.8    -38.79
    123.95    -39.75
    123.99    -36.79

Looks good.  Now let's actually work with a file and try the same thing. To open the file you need to use the following :

    f = open("sample_100.txt")
    for s in f:
        print s

You will get something like this:

    ...

    120.16	-39.48

    120.25	-37.67

    120.26	-36.92

    ...

Cool, huh?

Now what if want to do something useful, like **count** the number of lines in the file?  The naive approach is to just count the lines.

    f = open("sample_100.txt")

    line_count = 0
    for s in f:
        line_count+=1

    print line_count

Nice, way to go!  But we can do something a little better - that is we can load all the lines into a list.  Try this:


    f = open("sample_100.txt")
    file_as_list = f.readlines()

    print file_as_list # ==> ['120.04\t-42.8\n', '120.16\t-39.48\n', '120.25\t-37.67\n' ...]
    print len(file_as_list) # ==> 100


Notice that the strings in the list include '\t' and '\n' (tab and newline, respectively).  Let's work a little example to see what we can do to convert this string into something more useful.

Let's say we want to split this string along the tab character.  Doing so could not be simpler, let see:

    example = file_as_list[0] # ==> '120.04\t-42.8\n'
    print example.split('\t') # ==> pass in the character you want Python to split the string on (it could be anything, but we want '\t'
                              # ==> ['120.04', '-42.8\n']

This is nice -- but what if we wanted to turn this into a tuple.  Remember we can turn a list into a tuple (and visa versa):

    my_tuple = tuple(example.split('\t')) # ==> ('120.04', '-42.8\n')

In this case, we don't gain anything by converting to a tuple, but this can noneless be interesting down the road.  Notice something interesting here -- that is there is a '\n' at the end of the second string.  This is the newline character that was in the original file.  Unfortunately, this character is still with us and we really don't want it to be.  Never fret, there is an easy way out.  All strings have a method called `strip()` that will removed _whitespace characters_ (spaces, newlines, tabs) from the _beginning_ **and** _end_ of the string like so:

    # remove the whitespace (including newlines)
    example = file_as_list[0].strip()
    print example # ==> '120.04\t-42.8'

    # now we can split the string to make a list
    print example.split('\t') # ==> ['120.04', '-42.8']

### Lists again ...
As we can see, lists are really important in Python.  So much so that the language has provided a shortcut to making lists easier when you need to compose one fast.  Let say we want to take the **list of strings** and make that a **list of lists**.  In other words, let's say we want our file to look like the list: [['120.04', '-42.8'], ['120.16', '-39.48'], ...].  Getting the list os strings into this form could be very valuable for searching, sorting, etc. down the road.  Let's look at the straightforward way to do this with just loops:

    list_of_lists = []
    for s in file_as_list:
        s_split = s.strip().split('\t') # ==> ['120.04', '-42.8']
        list_of_lists.append(s_split)

Which gives us what we want:

    [['120.04', '-42.8'],
     ['120.16', '-39.48'],
     ['120.25', '-37.67'],
     ['120.26', '-36.92'],
     ['120.26', '-36.7'],
     ['120.3', '-39.67'],
     ['120.34', '-37.69'],
        ...
    ]

There is a shorthand way to do the same thing _in one line_ using what Pythonistas call **list comprehensions**.  Don't let the fancy name fool you -- this is a useful technique that will make your life easier and code more readable and compact.  To convert the loop above into a **list comprehension** we first must think from the outside and work our way in.  Let's say we want to make an empty list `[]` and inside that list we want to have the items of the list look like `['first_string', 'second_string']`.

Consider what the loop fragment `for s in file_list` does.  It gives us the string `'120.04\t-42.8\n'` for each item in file list.  Let's assume for a minute that we're allowed to do __one thing__ to each of those items in the loop.  What would it be?  In our case, we want to strip whitespace and split the string at the tab to get the resulting list (`['120.04', '-42.8']`).  Thus, that one thing looks like this `s.strip().split('\t')`.  Now what we want is just that list of all those two-element list of strings.  Thus, if we put all that together:

    list_of_lists = [ s.strip().split('\t')  for s in file_list ]
    print list_of_lists

which gives us :

    [['120.04', '-42.8'],
     ['120.16', '-39.48'],
     ['120.25', '-37.67'],
     ['120.26', '-36.92'],
     ['120.26', '-36.7'],
     ['120.3', '-39.67'],
     ['120.34', '-37.69'],
        ...
    ]


Awesome!

## Back to files
Now let's get back to files and introduce a few typical text file types.  Most of your data will come as a CSV, TSV or something similar


|File type  |   |   Looks like |
|----|----|-----|
|CSV  |Comma Separated Values | `a, b, c`  |
|TSV  |Tab Separated Values   | `a <tab> b <tab> c` |

Python provides a library for specifically working with CSV files, which will greatly reduce the amount of work you will be doing to work with the files.  Later when we move to Pandas, we'll advance our knowledge even further and dispense with the pleasantries of caring about the details of the CSV altogether.

For now, though, let's get a quick understanding of working with a CSV file.

### The `csv` library

When you are clear of the basics of files, you can forget what you know and move on to the `csv` library -- which takes even more work off your hands.  Essentially this library raises the bar a bit more and allows you to perform some more abstractions on the file.  In particular the library (despite its name) allows you to process CSV, TSV and any the xSV file that has a well known delimiter ('|', '~', etc.).

The code will look a lot like your previous code, but with some extra niceties:

    import csv
    with open('../data/sample_data.txt') as f:
        csv_reader = csv.reader(f, delimiter='\t') # necessary because the file is TAB delimited

        for l in csv_reader:
            print l

Will give you something like:

    ['120.04', '-42.8']
    ['120.16', '-39.48']
    ['120.25', '-37.67']
    ['120.26', '-36.92']
    ['120.26', '-36.7']
    ['120.3', '-39.67']
    ['120.34', '-37.69']
    ['120.4', '-40.55']
    ['120.4', '-36.37']
    ...

This may seem unremarkable but the advantage now is that we can assign the columns a name and then reference the data by name instead of index.  So using the DictReader` and optional parameter `fieldnames` we can give the fields whatever name we want and then access them by that name,

    import csv
    with open('../data/sample_data.txt') as f:
        csv_reader = csv.DictReader(f, delimiter='\t', fieldnames=['lat', 'lon'])

        for l in csv_reader:
            print l['lat'] # instead of l[0]

You might be wondering, **what if** the file already has a header row ... then we just omit the `fieldnames` and use the names in the header row:


    import csv
    with open('../data/sample_data.txt') as f:
        csv_reader = csv.DictReader(f, delimiter='\t')

        for l in csv_reader:
            print l['lat'] # instead of l[0]

Go check out the [Jupyter NB on file basics](./code/file_basics.ipynb) for more fun!