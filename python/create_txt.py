import os
man=[]
other=[]
os.chdir('chapter3')
try:
    data=open('data.txt')
    for each_line in data:
        try:
            #使用':'对字符串进行分割，前部分赋值给role，后部分赋值给line_spoken。'1'代表只对一行中第一个':'进行分割，
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')
print(man)
print(other)


try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)

except IOError:
    pirnt('file error')
finally:
    man_file.close()
    other_file.close()
