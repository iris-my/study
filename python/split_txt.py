import os

os.chdir('chapter3')
try:
   data=open('data.txt')

   for each_line in data:
'''if each_line.find(':')!=-1:   '''
      try:
         (role,line_spoken)= each_line.split(':',1)
         print(role,end='')
         print(' said: ',end='')
         print(line_spoken,end='')
      except ValueError:
         pass
    data.close()
except IOError:
    print('the data file is missing')
