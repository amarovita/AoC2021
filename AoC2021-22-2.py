data = open("AoC2021-22.input").read()

data = [x.split() for x in data.strip().splitlines()]

data = [(x=='on', tuple(tuple(map(int, z.split('=')[-1].split('..'))) for z in y.split(','))) for x, y in data]

data = data[::-1]

intervals = [[], [], []]
for c in data:
    for x in range(3):
        intervals[x].append(c[1][x][0])
        intervals[x].append(c[1][x][1]+1)

for x in range(3):
    intervals[x] = sorted(set(intervals[x]))

for x in range(3):
    intervals[x] = list(zip(intervals[x], intervals[x][1:]))

t = 0
for x in intervals[0]:
    print(f"\r{x[0]:8}", end='', flush=True)
    datax = [c for c in data if x[0]>=c[1][0][0] and x[1]<=c[1][0][1]+1]
    if not datax:
        continue
    for y in intervals[1]:
        datay = [c for c in datax if y[0]>=c[1][1][0] and y[1]<=c[1][1][1]+1]
        if not datay:
            continue
        for z in intervals[2]:
            try:
                dataz = next(c for c in datay if z[0]>=c[1][2][0] and z[1]<=c[1][2][1]+1)
                if dataz[0]:
                    t += (x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])
            except:
                ...
        
print(f"\r{' ':24}")
print(t)
