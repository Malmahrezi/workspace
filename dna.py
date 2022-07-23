import csv
from sys import argv

def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Incorrect # of inputs")
        exit()

    # TODO: Read database file into a variable
    with open(argv[1]) as e:
        reader = csv.DictReader(e)
        database = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2]) as f:
        sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}

    #This results in "name" : 0
    for i in database[0]:
        matches[i] = (longest_match(sequence, i))

    # TODO: Check database for matching profiles
    # Counter starts at 1, since there won't be a 'name' match
    suspect = 'No Match'
    suspect_counter = 1

    for i in range(len(database)):
        for j in matches:
            #Matches values are ints, need to cast them to strings for comparison
            if str(matches[j]) == database[i][j]:
                suspect_counter += 1
        if suspect_counter == len(matches):
            #We've got the suspect!  No need to continue
            suspect = database[i]['name']
            break
        else:
            suspect_counter = 1

    print(suspect)

    return