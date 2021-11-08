import datetime
from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()
diff_outputfile = "Mustafa.txt"
today_date = today.strftime("%m/%d/%Y")
time_now = now.strftime("%H:%M:%S")
diffcmd = "diff /home/op/product_test/workdir/WSISJCTXT.energy-gfs-db1 /home/op/product_test/workdir/WSISJCTXT.18.212.5.40 > /home/op/product_test/workdir/WSISJCTXT.diffs"
textproduct_filepath1 = "file1.txt"
textproduct_filepath2 = "file2.txt"
number_of_file1_lines = 5
number_of_file2_lines = 5
file_size1 = 30
file_size2 = 30
number_of_diff_lines = 2
difference_percentage = 0.4

line_to_add = ''
line_to_add+= ("-"*79 + "\n")
line_to_add+= f"|File Name: {diff_outputfile:33}|Date: {today_date:10} |Time: {time_now:8}|\n"
line_to_add+=  ("-"*79 + "\n")
line_to_add+= f"\ncommand Used: {diffcmd} \n"
line_to_add+= "\nFiles participate in diff\n"

line_to_add+= ("-"*79 + "\n")
line_to_add+= f"|File Name:                 |No. of Lines                       |File size    |\n"
line_to_add+= ("-"*79 + "\n")
line_to_add+= f"|{textproduct_filepath1:27}|{number_of_file1_lines:^34} |{file_size1:^13}|\n"
line_to_add+= f"|{textproduct_filepath2:27}|{number_of_file2_lines:^34} |{file_size2:^13}|\n"
line_to_add+= ("-"*79 + "\n")

line_to_add+= ("-"*79 + "\n")
line_to_add+= f"|Number of different lines = {number_of_diff_lines: <49}|\n"
line_to_add+= ("-"*79 + "\n")
line_to_add+= f"|Diff percentage = {difference_percentage: <59.0%}|\n"
line_to_add+= ("-"*79 + "\n")
print(line_to_add)
