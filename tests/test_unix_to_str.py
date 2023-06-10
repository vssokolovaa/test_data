from tests.dates import segment_1,segment_2,segment_3
from datetime import datetime


def test_unix_1():
    list_str_1 = []
    for i in range(0, len(segment_1)):
        list_str_1.append(datetime.utcfromtimestamp(int(segment_1[i])).strftime('%Y-%m-%d %H:%M:%S'))
    print('\n list_str_1==', list_str_1)


def test_unix_2():
    list_str_2 = []
    for i in range(0, len(segment_2)):
        list_str_2.append(datetime.utcfromtimestamp(int(segment_2[i])).strftime('%Y-%m-%d %H:%M:%S'))
    print('\n list_str_2==', list_str_2)


def test_unix_3():
    list_str_3 = []
    for i in range(0, len(segment_3)):
        list_str_3.append(datetime.utcfromtimestamp(int(segment_3[i])).strftime('%Y-%m-%d %H:%M:%S'))
    print('\n list_str_3==', list_str_3)
