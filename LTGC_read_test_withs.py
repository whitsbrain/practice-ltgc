
# This code reads each line in a file, looks for the first ".", then splits the line when it finds the first
# occurrence of the ".".  Then it writes the second variable of the split to a new file.  If it finds no ".",
# it just writes the entire line that it originally read.

# Opens file for reading.  The "with" statement makes sure the file is closed when finished reading
with open("ltgc_test.csv", "r") as ltgc_file:
    # Opens file for writing.  The "with" statement makes sure the file is closed when finished writing
    with open("ltgc_test_write6.csv", "w") as write_file:
        for i in ltgc_file:
            # look for the first "." in each line that is read from the opened file
            if "." in i:
                # split the variable into two at the first occurrence of "."
                number, episode = i.split(".", 1)
                # write the second variable of the split
                write_file.write(str(episode))
            else:
                # just write the original line if there's no "."
                write_file.write(str(i))
