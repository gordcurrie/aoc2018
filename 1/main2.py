import datetime

start = datetime.datetime.now()

fname = "./data.txt"

val = 0
vals = []
found = False
loop = 0

with open(fname) as f:
    content = f.read().splitlines()

intcontent = []
for x in content:
    intcontent.append(int(x))

while not found:
    for x in intcontent:
        val = val + x
        if val in vals:
            print("true")
            print(val)
            found = True
            break
        vals.append(val)

print((datetime.datetime.now()-start).total_seconds())
