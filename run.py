print("Hello World")

"""
This function reads data from a file outside the python file but inside our projrct.
We put a list of the days of the week.
"""
def check_data():
    file_input = open("days.txt", 'r')
    data = file_input.read()
    print(data)


"""
This function reads from a different txt file in our project, and we have asked it only
to read one line from the text.
"""
def read_lines():
    file_read = open("read.txt", 'r')
    info = file_read.readline()
    print(info)

"""
This function only reads the file up till 20 bytes & then stops.
"""
def read_20lines():
    file_read_20 = open("read.txt", 'r')
    sale = file_read_20.readlines(20)
    print(sale)



check_data()
#read_lines()
read_20lines()