import datetime
import string

start_at = datetime.datetime.now()

fname = "./data.txt"


with open(fname) as f:
    content = f.read().splitlines()

s = 1000
m = [[0 for x in range(s)] for y in range(s)]

for line in content:
    components = line.split(" ")
    start = components[2].split(":")[0].split(",")
    size = components[3].split("x")
    w = int(size[0])
    h = int(size[1])
    x = int(start[0])
    y = int(start[1])

    for i in range(x, x + w):
        for j in range(y, y + h):
            m[i][j] += 1

for line in content:
    components = line.split(" ")
    claim = components[0]
    start = components[2].split(":")[0].split(",")
    size = components[3].split("x")
    w = int(size[0])
    h = int(size[1])
    x = int(start[0])
    y = int(start[1])

    good = True
    for i in range(x, x + w):
        for j in range(y, y + h):
            if m[i][j] > 1:
                good = False

    if good:
        print(claim)

print((datetime.datetime.now()-start_at).total_seconds())
