"""
Print a nested list
"""

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item,end='   ')  
"""
print(each_item,end='   ')
Use TAB to print a nested list ,rather than simply a newline
"""

