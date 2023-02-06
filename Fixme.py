#!/usr/bin/python3

def evens(n):
    lst = []
    for i in range(n+1):
        if i%2 == 0:
            lst.append(i)
    return lst
