
# This code reads each line in a file, looks for a lead space, then writes everything but the lead space
# of that line to a new file.  If it finds no space, it just writes the entire line that it originally read.

# Opens file for reading.  The "with" statement makes sure the file is closed when finished reading
with open("ltgc_test_write6.csv", "r") as ltgc_file:
    # Opens file for writing.  The "with" statement makes sure the file is closed when finished writing
    with open("ltgc_test_remove_lead_space1.csv", "w") as write_file:
        for i in ltgc_file:
            # look for a leading space in each line that is read from the opened file
            if " " in i[0]:
                # make new variable with everything from the original line except for the lead space
                rem_lead_space = i[1:]
                # write the line without the lead space
                write_file.write(str(rem_lead_space))
            else:
                # just write the original line if there's no lead space
                write_file.write(str(i))
