#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import division
from timeit import Timer

multiply_by_10 = lambda x: 10 * x
run_range = range(0, 1000)

def for_traditional():
    for i in run_range:
        multiply_by_10(i)

def for_listcomp():
    [multiply_by_10(i) for i in run_range]

def create_table_result(title, results):
    head = 'min mean max'.split(' ')
    calc = {
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    print '\nResultados para: %s' % title
    print '{0:<10s} {1:<10s} {2:<10s}'.format(*head)
    print '{min:<10.5f} {mean:<10.5f} {max:<10.5f}'.format(**calc)

def profile(stmt='pass', setup='pass'):
    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r)

print 'Processando uma lista de 1000 elementos. Repetindo 10 vezes, 1000 execuções.'
profile('for_traditional()', 'from __main__ import for_traditional')
profile('for_listcomp()', 'from __main__ import for_listcomp')
