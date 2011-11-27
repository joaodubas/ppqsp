#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
from timeit import Timer

multiply_by_10 = lambda x: 10 * x
run_range = range(0, 1000)

def for_traditional_with_lambda():
    for i in run_range:
        multiply_by_10(i)

def for_listcomp_with_lambda():
    [multiply_by_10(i) for i in run_range]

def for_traditional():
    for i in run_range:
        10 * i

def for_listcomp():
    [10 * i for i in run_range]

def create_table_result(title, results):
    head = 'fn min mean max'.split(' ')
    calc = {
        'fn': title,
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    sys.stdout.write('{0:>30s} {1:<10s} {2:<10s} {3:<10s}'.format(*head))
    sys.stdout.write('\n{fn:>30s} {min:<10.8f} {mean:<10.8f} {max:<10.8f}\n'.format(**calc))

def profile(stmt='pass', setup='pass'):
    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r)

if __name__ == '__main__':
    # sys.stdout.write(u'Processando uma lista de 1000 elementos. Repetindo 10 vezes, 1000 execuções.\n')
    fn_list = 'for_traditional for_traditional_with_lambda for_listcomp for_listcomp_with_lambda'.split(' ')
    for fn in fn_list:
        profile('{}()'.format(fn), 'from __main__ import {}'.format(fn))
