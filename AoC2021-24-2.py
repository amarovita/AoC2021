from functools import lru_cache

def gosub(z, w, x0, w0):
    x = (z % 26) + x0
    if x0 < 0:
        z //= 26
    if w != x:
        z = 26 * z + w + w0
    return z

cf = [
    (12, 7),
    (11, 15),
    (12, 2),
    (-3, 15),
    (10, 14),
    (-9, 2),
    (10, 15),
    (-7, 1),
    (-11, 15),
    (-4, 15),
    (14, 12),
    (11, 2),
    (-8, 13),
    (-10, 13),
]

@lru_cache(maxsize=None)
def check2(t, cf):
    if not cf:
        return []
    c = cf[0]
    for n in range(1, 10):
        for z in range(10000):
            if gosub(z, n, c[0], c[1]) == t:
                r = check2(z, cf[1:])
                if r is not None:
                    return [n] + r
    return None


print(''.join(map(str, check2(0, tuple(cf[::-1]))))[::-1])




