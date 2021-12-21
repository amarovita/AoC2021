data = open("AoC2021-19.input").read()
data = [d.strip().splitlines()[1:] for d in data.strip().split('\n\n')]

data = [[list(map(int, p.split(','))) for p in s] for s in data]

ROT = (
    ((0,1,2), (1, 1, 1)),
    ((0,2,1), (1, 1, -1)),
    ((0,1,2), (1, -1, -1)),
    ((0,2,1), (1, -1, 1)),

    ((0,1,2), (-1, -1, 1)),
    ((0,2,1), (-1, -1, -1)),
    ((0,1,2), (-1, 1, -1)),
    ((0,2,1), (-1, 1, 1)),

    ((1,2,0), (1, 1, 1)),
    ((1,0,2), (1, 1, -1)),
    ((1,2,0), (1, -1, -1)),
    ((1,0,2), (1, -1, 1)),

    ((1,2,0), (-1, -1, 1)),
    ((1,0,2), (-1, -1, -1)),
    ((1,2,0), (-1, 1, -1)),
    ((1,0,2), (-1, 1, 1)),

    ((2,0,1), (1, 1, 1)),
    ((2,1,0), (1, 1, -1)),
    ((2,0,1), (1, -1, -1)),
    ((2,1,0), (1, -1, 1)),

    ((2,0,1), (-1, -1, 1)),
    ((2,1,0), (-1, -1, -1)),
    ((2,0,1), (-1, 1, -1)),
    ((2,1,0), (-1, 1, 1)),
)

def qdist(p1, p2):
    return sum((c1-c2)*(c1-c2) for c1, c2 in zip(p1, p2))

def mdist(p1, p2):
    return sum(abs(c1-c2) for c1, c2 in zip(p1, p2))

def invar(s):
    ret = []
    for x in range(len(s)-1):
        for y in range(x+1, len(s)):
            ret.append(qdist(s[x], s[y]))
    return sorted(ret)

def invar2(s, ndx):
    ret = []
    for x in range(len(s)):
        if x != ndx:
            ret.append(qdist(s[x], s[ndx]))
    return sorted(ret)

def unite(i1, i2):
    t1 = i1[:]
    t2 = i2[:]
    ret = []
    while t1 and t2:
        if t1[0]<t2[0]:
            ret.append(t1[0])
            t1 = t1[1:]
        elif t1[0]>t2[0]:
            ret.append(t2[0])
            t2 = t2[1:]
        else:
            ret.append(t1[0])
            t1, t2 = t1[1:], t2[1:]
    ret.extend(t1)
    ret.extend(t2)
    return ret

def intersect(i1, i2):
    t1 = i1[:]
    t2 = i2[:]
    ret = []
    while t1 and t2:
        if t1[0]<t2[0]:
            # ret.append(t1[0])
            t1 = t1[1:]
        elif t1[0]>t2[0]:
            # ret.append(t2[0])
            t2 = t2[1:]
        else:
            ret.append(t1[0])
            t1, t2 = t1[1:], t2[1:]
    return ret

def align(p1, p2, history):
    mx, mi, mj  = -1, 0, 0
    for i in range(len(p1)):
        for j in range(len(p2)):
            x = len(intersect(invar2(p1, i), invar2(p2, j)))
            if mx < x:
                mx, mi, mj = x, i, j
                if mx >= 12:
                    break
        else:
            continue
        break
    shftall = p1[mi][:]
    shftnew = p2[mj][:]
    p1 = sorted([[x-y for x, y in zip(z, p1[mi])] for z in p1])
    p2 = [[x-y for x, y in zip(z, p2[mj])] for z in p2]
    mx, rp  = -1, None
    for r in ROT:
        rr = sorted(rot(p2, r))
        ii = len(intersect(p1, rr))
        if ii > mx:
            shftrot = r
            mx, rp = ii, rr
            if mx >= 12:
                break
    p1 = sorted([[x+y for x, y in zip(z, shftall)] for z in p1])
    rp = sorted([[x+y for x, y in zip(z, shftall)] for z in rp])
    return p1, rp, history + [[shftall, shftnew, shftrot]]

def rot(p, r):
    ret = []
    for x in p:
        y = [x[k] for k in r[0]]
        ret.append([a*b for a, b in zip(y, r[1])])
    return ret

def derot(p, r):
    ret = []
    for x in p:
        y = [a*b for a, b in zip(x, r[1])]
        xr = [r[0].index(k) for k in range(3)]
        y = [y[k] for k in xr]
        # y = [y[k] for k in r[0]]
        ret.append(y)
    return ret

oops = data[0]
data = data[1:]
oopsy = invar(oops)
history=[]
while data:
    invd = invar(data[0])
    if len(intersect(oopsy, invd)) >= 66:
        s, *data = data
        print(len(data), '.', end='', flush=True)
        oops, s, history = align(oops, sorted(s), history)
        oops = unite(oops, s)
        oopsy = invar(oops)
    else:
        data = data[1:] + data[:1]
print()
print(len(oops))


res = [[0,0,0]]
p = [0,0,0]
for h in history:
    rr = rot([[-x for x in h[1]]], h[2])[0]
    dr = [x + y for x, y in zip(rr, h[0])]
    res.append(dr[:])
print(res)
print(max(mdist(x,y) for x in res for y in res))

