#!/usr/bin/python
#coding=utf8
def square(n):
    """Returns the square of a number."""
    squared = n**2
    #%d 是整形通配符
    print "%d squared is %d." %(n,squared)
    return squared
square(10)
