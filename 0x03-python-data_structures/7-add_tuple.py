def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    c = tuple(x + y for x, y in zip(a, b))

    return c[:2]
