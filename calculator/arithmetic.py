#!/usr/bin/python3

def add(*args):
    result = 0
    for value in args:
        result = result + value
    return(result)

def mul(*args):
    result = 1
    for value in args:
        result = result * value
    return(result)

def div(*args):
    result = 1
    for value in args:
        result = value / result
    return(result)

def sub(*args):
    result = 0
    for value in args:
        result = value - result
    return(result)


