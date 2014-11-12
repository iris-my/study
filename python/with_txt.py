import os

try:
    data=open('chapter3/its.txt','w')
    print("It's..",file=data)
except IOError as err:
    print('file error:' + str(err))
finally:
    if 'data' in locals():
        data.close()



#使用with语句，就不再需要包含一个finally组来处理文件的关闭，及妥善关闭一个可能打开的数据文件
try:
    with open('chapter3/with.txt','w') as data:
        print("with file ...",file=data)
except IOError as err:
    print('file error:' + str(err))

