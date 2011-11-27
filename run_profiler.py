#!/usr/bin/env python
from profiler.decorator import profile
from class_0 import for_profiler

@profile('profile.prof')
def runner(fn):
    for i in range(0, 1000):
        fn()

runner(for_profiler.for_traditional)
runner(for_profiler.for_listcomp)
