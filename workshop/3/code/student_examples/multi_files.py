'''
    Say you have a bunch of files named my_file_1, my_file_2, etc.

    If you know the basic structure of the file and the numbers you need,
    one easy way is to

    1. create a list of the numbers you want to process
    2. iterate over those file names

    See the code below
'''
def process_files():

    '''
        In this case we assume the filenames are of the form:

            my_file_1.txt
            my_file_2.txt
            ... and so on

    '''
    file_base = "my_file_"
    list_of_numbers = [1,2,3,4,5]

    for n in list_of_numbers:
        with open(file_base + str(n) + ".txt") as f:
            data = f.readlines()
            ''' load file data and plot commands here '''


'''
    Another way to solve the same problem is to use the glob library in Python.
    (see more at https://docs.python.org/2.7/library/glob.html).

    With this method may use any pattern we'd like to find the files we're interested
    in opening.  In this case we're using the pattern:

        my_file_?.txt

'''
def process_files_with_glob():
    ### The glob way ###
    import glob

    file_base_pattern = "my_file_?.txt" # what we're doing here is putting a wildcard ? in the place of the number in the name
    for f in glob.iglob(file_base_pattern):
        with open(f) as datafile:
            datafile.readlines()
