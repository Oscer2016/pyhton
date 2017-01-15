#!/usr/bin/env python
# coding=utf-8

def fact(n):
    print 'n=',n
    if n > 1 :
        return n * fact(n-1)
    else:
        print 'end of the line'
        return 1

if __name__ == "__main__":
    n = 5
    print 'fact(n) = %d' % fact(n)
