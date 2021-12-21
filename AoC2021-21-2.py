from functools import lru_cache
from collections import defaultdict 


@lru_cache(maxsize=None)
def wins2(p1, s1, p2, s2,  n=1):
    ret1 = defaultdict(int)
    ret2 = defaultdict(int)
    # if n<10:
    print('DICE', end='', flush=True)
    for dice in range(27):
        # if n<10:
        print(f'\b\b\b\b{dice:4}', end='', flush=True)
        sumdice = 3 + dice % 3 + dice // 3 % 3 + dice // 9 % 3
        np1 = (p1 - 1 + sumdice) % 10 + 1
        ns1 = s1 + np1
        if ns1 >= 21:
            ret1[n] += 1
        else:
            for dice2 in range(27):
                sumdice = 3 + dice2 % 3 + dice2 // 3 % 3 + dice2 // 9 % 3
                np2 = (p2 - 1 + sumdice) % 10 + 1
                ns2 = s2 + np2
                if ns2 >= 21:
                    ret2[n] += 1
                else:
                    sub1, sub2 = wins2(np1, ns1, np2, ns2, n+1)
                    for w in sub1:
                        ret1[w] += sub1[w]
                    for w in sub2:
                        ret2[w] += sub2[w]
    # if n<10:
    print('\b\b\b\b    \b\b\b\b', end='', flush=True)
    return ret1, ret2

r1, r2 = wins2(10,0,7,0)
print()
print(sum(r1.values()), sum(r2.values()))
