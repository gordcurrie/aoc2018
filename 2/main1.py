import datetime
import string

start = datetime.datetime.now()
counts = dict.fromkeys(list(range(9)), 0)

fname = "./data.txt"

val = 0

with open(fname) as f:
    content = f.read().splitlines()

for line in content:
    repeated_letters = dict.fromkeys(string.ascii_lowercase, 0)
    for letter in line:
        repeated_letters[letter] += 1

    inner_count = dict.fromkeys(list(range(9)), 0)
    for key, value in repeated_letters.items():
       inner_count[value] = 1

    for key, value in inner_count.items():
        if key > 1 and value > 0:
            counts[key] += 1

total = 1
for key, value in counts.items():
    if value > 0:
        total = total * value

print(total)

print((datetime.datetime.now()-start).total_seconds())
