import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 2 3 4 5'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.evenlist[0] == 1
    assert main.main.evenlist[1] == 3
    assert main.main.evenlist[2] == 5


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 3 5 4 2 7 8 1 2 5'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
    assert main.main.evenlist[0] == 1
    assert main.main.evenlist[1] == 5
    assert main.main.evenlist[2] == 2
    assert main.main.evenlist[3] == 8
    assert main.main.evenlist[4] == 2
