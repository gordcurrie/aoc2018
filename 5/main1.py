from datetime import datetime
import string
import re
import copy

def same_letter(a, b):
    return a.lower() == b.lower()

def opposite_case(a, b):
    return a.isupper() and b.islower() or a.islower() and b.isupper()

def match(a, b):
    return opposite_case(a, b) and same_letter(a,b)

start_at = datetime.now()

fname = "./data.txt"

with open(fname) as f:
    content = f.read()

as_list = list(content)

has_changes = True
while has_changes:
    has_changes = False
    for idx, char in enumerate(as_list):
        if idx < len(as_list) - 1:
            if match(char, as_list[idx + 1]):
                has_changes = True
                as_list[idx] = ""
                as_list[idx + 1] = ""
    content = ''.join(as_list)
    as_list = list(content)

content = ''.join(as_list)
print(len(content) - 2)
print(content)
print((datetime.now()-start_at).total_seconds())
