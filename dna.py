import csv
from sys import argv

def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Incorrect # of inputs")
        exit()

    # TODO: Read database file into a variable
    with open(argv[1]) as e:
        reader = csv.reader(e)
        database = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2]) as f:
        sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    matches = []
    for i in range(1, len(database[0])):
        matches.append(longest_match(sequence, database[0][i]))


    # TODO: Check database for matching profiles
    suspect = 'No Match'
    suspect_counter = 0

    for i in range(1, len(database)):
        for j in range(len(matches)):
            #special note, the database is all strings, so int() is required to
            #convert from string to int
            if matches[j] == int(database[i][j+1]):
                suspect_counter += 1

        if suspect_counter == len(matches):
            # We've got the suspect!  No need to continue.
            suspect = database[i][0]
            break
        else:
            suspect_counter = 0
    print(suspect)

    return

    print(suspect)

    return