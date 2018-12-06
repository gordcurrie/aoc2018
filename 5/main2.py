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

letters = list(string.ascii_lowercase)

start_at = datetime.now()

fname = "./data.txt"

with open(fname) as f:
    content = f.read()

best_letter = "#"
best_letter_length = len(content)

for letter in letters:
    new_content = content
    new_content = new_content.replace(letter, "")
    new_content = new_content.replace(letter.upper(), "")
    as_list = list(new_content)
    has_changes = True
    while has_changes:
        has_changes = False
        for idx, char in enumerate(as_list):
            if idx < len(as_list) - 1:
                if match(char, as_list[idx + 1]):
                    has_changes = True
                    as_list[idx] = ""
                    as_list[idx + 1] = ""
        c = ''.join(as_list)
        as_list = list(c)
    if len(as_list) - 2 < best_letter_length:
        best_letter_length = len(as_list) - 2
        best_letter = letter
    print("{}: {:d}".format(letter, len(as_list)))
    print((datetime.now()-start_at).total_seconds())

print("=====================================")
print(best_letter)
print(best_letter_length)
print("=====================================")
