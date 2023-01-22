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

    regex_string = r'[\w,\W]*5'
    regex_string += r'[\w,\W]*4'
    regex_string += r'[\w,\W]*3'
    regex_string += r'[\w,\W]*2'
    regex_string += r'[\w,\W]*1'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '90\n10\n50\n40\n30'
    datastr = '1 5 2 8 2'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    regex_string = r'[\w,\W]*2'
    regex_string += r'[\w,\W]*8'
    regex_string += r'[\w,\W]*2'
    regex_string += r'[\w,\W]*5'
    regex_string += r'[\w,\W]*1'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())
