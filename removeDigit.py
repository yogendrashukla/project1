import re
from string import digits


def remove(list):
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list]
    return list


list = ['4geeks', '3for', '4geeks']
print(remove(list))


def Remove(list):
    list = [''.join(x for x in i if x.isalpha()) for i in list]
    return list


list = ['4geeks', '3for', '4geeks']
print(Remove(list))
def REMOVE(list):
    remove_digit=str.maketrans('','',digits)
    list=[i.translate(remove_digit) for i in list]
    return list;


list = ['4geeks', '3for', '4geeks']
print(REMOVE(list))