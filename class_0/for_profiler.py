#!/usr/bin/env python
multiply_by_10 = lambda x: 10 * x

run_range = range(0, 1000)

def for_traditional():
    for i in run_range:
        multiply_by_10(i)

def for_listcomp():
    [multiply_by_10(i) for i in run_range]
