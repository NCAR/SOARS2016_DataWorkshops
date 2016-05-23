# What Python is about ...
First and foremost, Python is about readability.  You will soon find out that what makes Python interesting is _not_ its syntax.  Python is about expressing your ideas in the most direct way you can, and this is often counter to languages you may have worked with before.  If it looks that simple ... in Python, you must accept that truth and move on.  You will soon accept many truths of simplicity that you have been ignoring ... and you just might fall for Python as many, many other have.

# Basic Data Types

## Integers and Floats
As with almost all languages, support for numbers (integers, floats and others) is basic to the operation of the language.  In Python, you'll need to know about **integers**,

    # this is an integer
    silly_integer = 1

    another_silly_integer = 129834

When you need a little more precision, you will want to work with **floating point** numbers.  So if you need a decimal in your number, try

    # this is a float
    silly_float = 1.01

    # if you need a float
    another_silly_float = 1.

    # and another ...
    more_interesting_float = 78.23479478099

Intuitively, adding, subtracting and doing math operations work as expected :

    a = 1
    b = 1.25
    c = a + b
    print c # ==> 2.25 as expected

    c = a / b
    print c # ==> 0.8 as expected


## Strings
Strings are again, another crucial type built in to almost all languages.  In Python, they work as expected:

    first_name = "Bob"
    last_name = "Jones"

To take two strings and concatenate them (merge 2 or more strings together end-to-end):

    fullname = first_name + last_name
    print fullname # ==> "BobJones"

    fullname = first_name + " " + last_name
    print fullname # ==> "Bob Jones"


Later we will learn about some other useful operations on strings.


# Data Structures
As a Pythonista padwan there are three data structures you will need to know well:

* tuples,
* lists, and
* dictionaries.

## Tuples
A tuple is a ordered "list" of items, but unlike a list they can't be changed (also referred to as "immutable").  So it's not "really" a list, but "list" gives you a point of reference.

        # this is an empty tuple
        tpl = ()

        # you can add anything to your tuple; make a new one with what you want
        tpl1 = (1, 2, 1)

        # you can also make a new tuple from existing tuples
        tpl2 = (4, 5)
        tpl3 = tpl1 + tpl2 # ==> (1, 2, 1, 4, 5)

Tuples can contain whatever you'd like: numbers, strings, other objects (lists, dicts, other tuples), etc.  And you can mix and match.

        # a tuple of strings
        tpl1 = ("you", "are", "here")

        tpl2 = (1, "you", (0, 0, 0))

        tpl3 = (1, ["fred", "bob"], (3, 2))

## Lists
Lists are fun, they are sort of like tuples, except you can do a lot more with them and you can change them (they are referred to as "mutable").


        # this is an empty list
        lst = []

        # this is a list with a single item
        lst = [1]

        # this is a list with several items
        lst = [1, 2, 3, 4]

        # but a list can contain just about anything ... including other lists
        lst = [[1, 2, 3],[1],[4, [5, 6], 7]]

## Dictionaries

Dictionaries are even more fun - they contain a _key_ and a _value_ ... and are not unlike a _real_ dictionary except in a Python dictionary you can only have a single unique key, thus _unlike_ a real dictionary, the word "book" will only have a single entry.  Furthermore, the dictionary value can be nearly anything - another dictionary, list, etc.


### Initialization
There are a variety of ways to make dictionaries:

        # this is an empty dictionary
        dct = {}

        # this is a dictionary with a single key as a string and an integer value
        dct = {'book': 0}

        # here is another way to make a dictionary with a list of tuples
        dct = dict([('book', 0)])

        # and a really nice way to make a dictionary
        dct = dict(a=1, b=[1, 2], c={'book': 0}, d={'cat': 'dog'})

### Data access
Accessing a dictionary is easy with just referencing the key whose value you'd like to access:

        dct = dict(a=1, b=[1, 2], c={'book': 0}, d={'cat': 'dog'})

        dct['d'] # ==> {'cat': 'dog'}
        dct['a'] # ==> 1

        # there is also the get() method
        dct.get('a') # ==> 1
        dct.get('p') # ==> None


**A note about get() method:**  One thing I wish I had used more often in the beginning was `dict.get()`.  When accessing a value by it's key, if you try to access a key that does not exist, you will get a `KeyError` ... this is actually a good thing in some contexts, but in others, you may just want to know that the value exists without catching and handling the exception.  `get()` does this beautifully and additionally, if you want a value to be returned other than the default of `None`, then you can set the second parameter to just that value:

        dct['p'] # ==> KeyError: 'p'
        dct.get('p', -1) # ==> -1 instead of the default None


# Operating over data structures
I am assuming here (for now), the you have a basic understanding looping over things (at least abstractly).  Let's say, for example, you are interested in adding the numbers in a list of numbers.

Let's try:

        # starting with a tuple of numbers
        ton = (1, 2, 3, 4, 5)

What you want to do now is just print the numbers in that list:

    for number in ton:
        print number

That will give you the output:

    1
    2
    3
    4
    5

How about a list:

    lon = [1, 2, 3, 4, 5]

That will **_also_** give you the output:

    1
    2
    3
    4
    5

Now what about dictionaries?

    dct = {a: 1, b: 2, c: 3}
    for d in dct:
        print d

The result is:

    a
    c
    b

These are the **keys**, but what about the **values**?

When using a simple loop over the whole dictionary, you can use the dictionary method `iteritems()` and build the loop like this instead:

    for d, val in dct.iteritems():
        print d, val

Now gives us:

    a 1
    b 2
    c 3

