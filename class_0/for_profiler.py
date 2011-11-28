#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
from timeit import Timer

multiply_by_10 = lambda x: 10 * x
min_range = 0
max_range = 1000

def for_traditional_with_lambda():
    run_range = range(min_range, max_range)
    mul_range = []
    for i in run_range:
        mul_range.append(multiply_by_10(i))
    return mul_range

def for_traditional():
    run_range = range(min_range, max_range)
    mul_range = []
    for i in run_range:
        mul_range.append(10 * i)
    return mul_range

def for_traditional_with_lambda_same_list():
    run_range = range(min_range, max_range)
    for i, v in enumerate(run_range):
        run_range[i] = multiply_by_10(v)
    return run_range

def for_traditional_same_list():
    run_range = range(min_range, max_range)
    for i, v in enumerate(run_range):
        run_range[i] = v * 10
    return run_range

def for_listcomp_with_lambda():
    run_range = range(min_range, max_range)
    return [multiply_by_10(i) for i in run_range]

def for_listcomp():
    run_range = range(min_range, max_range)
    return [10 * i for i in run_range]

def create_table_result(title, results):
    head = 'fn min mean max'.split(' ')
    calc = {
        'fn': title,
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    sys.stdout.write('{0:>40s} {1:<10s} {2:<10s} {3:<10s}'.format(*head))
    sys.stdout.write('\n{fn:>40s} {min:<10.8f} {mean:<10.8f} {max:<10.8f}\n'.format(**calc))

def profile(stmt='pass', setup='pass'):
    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r)

if __name__ == '__main__':
    fn_list = 'for_traditional for_traditional_with_lambda for_traditional_same_list for_traditional_with_lambda_same_list for_listcomp for_listcomp_with_lambda'.split(' ')
    for fn in fn_list:
        profile('{}()'.format(fn), 'from __main__ import {}'.format(fn))
