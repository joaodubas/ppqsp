#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
from timeit import Timer

multiply_by_10 = lambda x: 10 * x
min_range = 0
max_range = 1000

def test_for_loop_with_lambda():
    run_range = range(min_range, max_range)
    mul_range = []
    for i in run_range:
        mul_range.append(multiply_by_10(i))
    return mul_range

def test_for_loop():
    run_range = range(min_range, max_range)
    mul_range = []
    for i in run_range:
        mul_range.append(10 * i)
    return mul_range

def test_for_loop_with_lambda_same_list():
    run_range = range(min_range, max_range)
    for i, v in enumerate(run_range):
        run_range[i] = multiply_by_10(v)
    return run_range

def test_for_loop_same_list():
    run_range = range(min_range, max_range)
    for i, v in enumerate(run_range):
        run_range[i] = v * 10
    return run_range

def test_listcomp_with_lambda():
    run_range = range(min_range, max_range)
    return [multiply_by_10(i) for i in run_range]

def test_listcomp():
    run_range = range(min_range, max_range)
    return [10 * i for i in run_range]

def create_table_result(title, results, **kwargs):
    fn_name_len = kwargs.pop('fn_name_len', len(title))
    head = 'fn min mean max'.split(' ')
    calc = {
        'fn': title,
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    sys.stdout.write('{0:>{fn_name_len}s} {1:<10s} {2:<10s} {3:<10s}'.format(fn_name_len=fn_name_len, *head))
    sys.stdout.write('\n{fn:>{fn_name_len}s} {min:<10.8f} {mean:<10.8f} {max:<10.8f}\n'.format(fn_name_len=fn_name_len, **calc))

def profile(stmt='pass', setup='pass', **kwargs):
    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r, **kwargs)

if __name__ == '__main__':
    fn_list = 'test_for_loop test_for_loop_with_lambda test_for_loop_same_list test_for_loop_with_lambda_same_list test_listcomp test_listcomp_with_lambda'.split(' ')
    fn_len = max([len(fn) for fn in fn_list]) + 2
    resp_list = [locals().get(fn)() for fn in fn_list]
    assert resp_list.count(resp_list[0]) == len(resp_list)

    for fn in fn_list:
        profile('{0}()'.format(fn), 'from __main__ import {0}'.format(fn), fn_name_len=fn_len)
