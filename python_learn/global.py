import sys
import test

a = 1

def func1():
    global  a
    a += 1

def func2():
    test.a += 1

def func3():
    module = sys.modules['test']
    module.a += 3

func1()
func2()
func3()
print a
print test.a
