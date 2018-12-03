import datetime

start = datetime.datetime.now()

fname = "./data.txt"

val = 0

with open(fname) as f:
    content = f.read().splitlines()

intcontent = []
for x in content:
    intcontent.append(int(x))

for x in intcontent:
    val = val + x

print(val)

print((datetime.datetime.now()-start).total_seconds())
