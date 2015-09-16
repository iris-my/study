import os
import re

words=input("Please input a word you want to search:")
thefile=open('/PythonStudy_dir/study/python/chapter3/data.txt','r').read()


line=re.split('[^a-zA-Z0-9\']',thefile)
count=0
for word in (line):
    if (word==words):
        count += 1
print(count)


