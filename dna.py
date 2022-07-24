from sys import argv
from sys import exit
import csv

def consecutive_count(str_sequence, dna_sequence):
    str_max_count = 0
    str_pattern = str_sequence

    while str_pattern in dna_sequence:
        str_max_count += 1
        str_pattern += str_sequence
    return str_max_count

if len(argv) != 3:
    print("Please include CSV and TXT file to command line")
    exit(1)

people = []
str_sequence = []
filename = argv[1]

with open(filename) as file:
    reader = csv.DictReader(file)
    for name in reader:
        people.append(name)

for i in dict.keys(people[0]):
    str_sequence.append(i)
str_sequence.pop(0)


txt = open(argv[2])
dna_sequence = txt.read()

str_count = dict.fromkeys(str_sequence, 0)

for i in range(len(str_sequence)):
    x = consecutive_count(str_sequence[i], dna_sequence)
    str_count[str_sequence[i]] = x


for i in range(len(people)):
    match_count = 0
    for j in range(len(str_sequence)):
        if int(people[i][str_sequence[j]]) == int(str_count[str_sequence[j]]):
            match_count += 1
            if match_count == len(str_sequence):
                print(people[i]['name'])
                exit(0)
        else:
            continue

print("No Match")