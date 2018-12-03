import datetime
import string

start = datetime.datetime.now()

fname = "./data.txt"

with open(fname) as f:
    content = f.read().splitlines()

for i, line in enumerate(content):
    for x in range(i + 1, len(content)):
        compare = content[x]
        different_count = 0
        holder = []
        for k, letter in enumerate(line):
            if letter != compare[k]:
                different_count += 1
            else:
                holder.append(letter)

        if different_count < 2:
            print("!!!!!!MATCHING!!!!!")
            print(line)
            print(compare)
            print(''.join(holder))


print((datetime.datetime.now()-start).total_seconds())
