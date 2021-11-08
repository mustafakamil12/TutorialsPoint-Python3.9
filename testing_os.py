import os

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def count_number_of_lines_in_file(thefilepath):
    count = 0
    file = open(thefilepath, 'rb')
    while 1:
        buffer = file.read(8192*1024)
        decoded_buffer = buffer.decode('utf-8')
        #print(f"buffer = {decoded_buffer}")
        if not decoded_buffer: break
        #print(decoded_buffer.count('\n'))
        count += decoded_buffer.count('\n')
    #print(f"count = {count}")
    file.close()
    return int(count)


textproduct_filepath1 = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/file1.txt"
textproduct_filepath2 = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/file2.txt"
cmd = "diff -y --suppress-common-lines %s %s | grep '^' | wc -l" % (textproduct_filepath1,textproduct_filepath2)
#print(cmd)
result = os.system(cmd)
print(f"result = {result}")

numberOfLines = count_number_of_lines_in_file(textproduct_filepath1)
print(numberOfLines)

no_lines1 = count_number_of_lines_in_file(textproduct_filepath1)
no_lines2 = count_number_of_lines_in_file(textproduct_filepath2)
no_diff = '2'
difference_percentage = int((int(no_diff) / no_lines1)*100)
line_to_add = ''
line_to_add += "Number of Lines in file1 = " + str(no_lines1) + "\t"
line_to_add += "Number of Lines in file2 = " + str(no_lines2)
len_of_info = len(line_to_add)
line_to_add += "\nNumber of different lines = " + no_diff + "\t"
line_spreator = ("-"*len_of_info)
line_to_add += "Diff percentage = " + str(difference_percentage) + "%" + "\n"
line_to_add += line_spreator
prepend_line(textproduct_filepath1,line_to_add)
