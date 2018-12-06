from datetime import datetime
import string
import re
import copy

start_at = datetime.now()

fname = "./data.txt"

with open(fname) as f:
    content = f.read().splitlines()

shifts = []
s = sorted(content)

current_shift = []
for line in s:
    if "#" in line:
        shifts.append(current_shift.copy())
        current_shift = []
        current_shift.append(line)
    else:
        current_shift.append(line)

    match = re.search('\[(.*?)\]', line)
    datetime_object = datetime.strptime(match.group(), '[%Y-%m-%d %H:%M]')

sleep = dict()
for shift in shifts:
    guard = 0
    for entry in shift:
        if "#" in entry:
            guard = re.search('\#\d*', entry)
            if guard:
                guard = int(guard.group(0).split("#")[1])
                sleep[guard] = [0 for x in range(60)]

for shift in shifts:
    guard = 0
    sleep_start = 0
    sleep_end = 0
    for entry in shift:
        if "#" in entry:
            guard = re.search('\#\d*', entry)
            if guard:
                guard = int(guard.group(0).split("#")[1])
        if "falls asleep" in entry:
            match = re.search('\[(.*?)\]', entry)
            datetime_object = datetime.strptime(match.group(), '[%Y-%m-%d %H:%M]')
            sleep_start = datetime_object.minute
        if "wakes up" in entry:
            match = re.search('\[(.*?)\]', entry)
            datetime_object = datetime.strptime(match.group(), '[%Y-%m-%d %H:%M]')
            sleep_end = datetime_object.minute
            for i in range(sleep_start, sleep_end):
                sleep[guard][i] += 1

max_sleep_minutes = 0
max_sleep_guard = 0
max_sleep_minute = 0

for guard, minutes in sleep.items():
    for idx, val in enumerate(minutes):
        if val > max_sleep_minutes:
            max_sleep_minutes = val
            max_sleep_minute = idx
            max_sleep_guard = guard

print(max_sleep_guard * max_sleep_minute)

print((datetime.now()-start_at).total_seconds())
