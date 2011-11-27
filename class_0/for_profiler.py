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
    head = 'min mean max'.split(' ')
    calc = {
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    sys.stdout.write('\nResultados para: %s' % title)
    sys.stdout.write('\n{0:<10s} {1:<10s} {2:<10s}'.format(*head))
    sys.stdout.write('\n{min:<10.5f} {mean:<10.5f} {max:<10.5f}\n'.format(**calc))

def profile(stmt='pass', setup='pass'):
    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r)

if __name__ == '__main__':
    sys.stdout.write('Processando uma lista de 1000 elementos. Repetindo 10 vezes, 1000 execuções.\n')
    fn_list = 'for_traditional for_traditional_with_lambda for_listcomp for_listcomp_with_lambda'.split(' ')
    for fn in fn_list:
        profile('{}()'.format(fn), 'from __main__ import {}'.format(fn))
