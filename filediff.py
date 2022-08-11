"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    if line1 == line2:
        return IDENTICAL
    elif len(line1) == len(line2):
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                return i
    else:
        if line1 in line2:
            return len(line1)
        elif line2 in line1:
            return len(line2)
        else:
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    return i
    
    
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx == IDENTICAL or idx > len(line2) or idx > len(line1):
        return ""
    new_line = "=" * idx + "^"
    return "{}\n{}\n{}\n".format(line1, new_line, line2)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    elif lines1 == [] or lines2 == []:
        return (0, 0)
    elif len(lines2) > len(lines1):
        for i in range(len(lines1)):
            if singleline_diff(lines1[i], lines2[i]) != IDENTICAL:
                return (len(lines1),singleline_diff(lines1[i], lines2[i]))
            else:
                return (len(lines1), 0)
    elif len(lines2) < len(lines1):
        for i in range(len(lines2)):
            if singleline_diff(lines1[i], lines2[i]) != IDENTICAL:
                return (len(lines2),singleline_diff(lines1[i], lines2[i]))
            else:
                return (len(lines2), 0)
    else:
        for i in range(len(lines1)):
            if singleline_diff(lines1[i], lines2[i]) != IDENTICAL:
                return(i, singleline_diff(lines1[i], lines2[i]))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename) as file:
    #file = open(filename, "rt")
        readfile = file.readlines()
    for i in range(len(readfile)):
        #if "\n" in line or "\t" in line:
        readfile[i] = readfile[i].replace("\n","")
        readfile[i] = readfile[i].replace("\t","")
    #file.close()
    return readfile


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    if file1 == file2:
        return "No differences\n"
    elif len(file1) < len(file2):
        for i in range(len(file1)):
            if singleline_diff(file1[i], file2[i]) != IDENTICAL:
                idx = singleline_diff(file1[i], file2[i])
                return "line{}\n{}".format(i, singleline_diff_format(file1[i], file2[i], idx))
    elif len(file1) == 0:
        return "Line {}:\n{}".format(0, singleline_diff_format("", file2[0], singleline_diff("",file2[0])))
    elif len(file2) == 0:
        return "Line {}:\n{}".format(0, singleline_diff_format(file1[0], "", singleline_diff(file1[0],"")))
    else:
        for i in range(len(file2)):
            if singleline_diff(file1[i], file2[i]) != IDENTICAL:
                idx = singleline_diff(file1[i], file2[i])
                return "Line {}:\n{}".format(i, singleline_diff_format(file1[i], file2[i], idx))
#print( file_diff_format('file8.txt', 'file9.txt'))
# for test_1, test_2 in [("file1.txt", "file2.txt"), ("file2.txt", "file3.txt"), ("file4.txt", "file5.txt"),
#                        ("file6.txt", "file7.txt"), ("file8.txt", "file9.txt"), ("file6.txt", "file10.txt")]:
# 	print(file_diff_format(test_1, test_2))
# 	# print(repr(file_diff_format(test_1, test_2)))
# 	print("******")