def readFile(file_name):
    f = open(file_name)
    content = f.read()
    print(content)
    return

readFile("Sample-Spreadsheet-10-rows-csv.txt")