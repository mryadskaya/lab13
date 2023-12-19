#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_abs_after_min(*args):
    if len(args) == 0:
        return None
    min_arg = min(args, key=abs)
    min_arg_index = args.index(min_arg)
    sum_of_abs = 0
    for i, arg in enumerate(args[min_arg_index + 1:]):
        sum_of_abs += abs(arg)
    return sum_of_abs

if __name__ == "__main__":
    p = list(int(i) for i in input("Введите значения: ").split())
    result = sum_of_abs_after_min(*p)
    print(result)



