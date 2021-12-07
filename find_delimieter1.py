from detect_delimiter import detect
import functools

def delimiter_cmp(a, b):
    print("comparing ", a, " and ", b)
    if a == b:
        print(0)
        return 0
    else:
        print(-1)
        return -1

def delimiter_compare(myfile_path):
    done = False
    myfile = open(myfile_path,'r')
    delimiter_array = []
    for line in myfile:
        #print(line)
        delimiter_detected = detect(line)
        print(f"delimiter is = '{delimiter_detected}'")
        delimiter_array.append(delimiter_detected)
    for curr_index in range(len(delimiter_array)):
        for next_index in range(curr_index+1,len(delimiter_array)):
            comp_res = delimiter_cmp(delimiter_array[curr_index],delimiter_array[next_index])
            if comp_res == 0:
                continue
            else:
                print("Discover delmiter difference...")
                done = True
                break
        if done == True:
            #break
            return -1,'-1'
    myfile.close()
    return 0,delimiter_detected;

#mydetect = detect("112321 01 KSBY  7   35   21  N-13  57")
#print(f"delmiter located  = '{mydetect}'")


file_path = "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/delim3.txt"
#print(myfile)
#myfile.close()
delimiter_res,delimiter_type = delimiter_compare(file_path)
print(f"delimiter_res = {delimiter_res}")
print(f"delimiter_type = {delimiter_type}")
