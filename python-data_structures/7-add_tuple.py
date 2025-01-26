#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_len = max(len(tuple_a), len(tuple_b))

    corregido1 = tuple_a + (2,) * (max_len - len(tuple_a))
    corregido2 = tuple_b + (2,) * (max_len - len(tuple_b))
    return tuple(a + b for a, b in zip(corregido1, corregido2))
