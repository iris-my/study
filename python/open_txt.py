import os

os.getcwd()
os.chdir('../chapter3')
os.getcwd()

"""
Open a file ,and the file content is assigned to a file object called data
"""
data=open('data.txt')
for each_line in data:
    print(each_line,end='')
data.close()


