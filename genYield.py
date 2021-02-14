"""
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    #print("result: ", result)
    return result
"""
def csv_reader(file_name):
    for row in open(file_name):
        yield row

csv_gen = csv_reader("1500000-Sales-Records-csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"row count is {row_count}")