import csv
import sys


def main():
    #ensuring that the correct number of command line arguments are given using len(argv)
    if len(sys.argv) < 3:
        print("Usage: python dna.py *.csv *.txt")
        sys.exit(1)
# Add database file into a variable
    database = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)
# Add DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        dna_sequence = file.read()
# check List of subsequences
    subsequences = list(database[0].keys())[1:]
# In DNA sequence Find longest match of each STR
    result = {}
    for subsequence in subsequences:
        result[subsequence] = longest_match(dna_sequence, subsequence)
# Find maching profile in the database
    for person in database:
        match = 0
        for subsequence in subsequences:
            if int(person[subsequence]) == result[subsequence]:
                match += 1
# If case that all subsequences matched
        if match == len(subsequences):
            print(person["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
# Creat variable
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
# To find the most consecutive runs of subsequence, Check each character.
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0
# Try to find a subsequence match in a subsent of characters, if you find a mach, move it to next potential match in the sequence, continue this proccess until the consecutive maches are finished.
        while True:
            # Set a substring start and end.
            start = i + count * subsequence_length
            end = start + subsequence_length
# If their is a match
            if sequence[start:end] == subsequence:
                count += 1
# If their is no match
            else:
                break
# Update most consecutive matches found
        longest_run = max(longest_run, count)
# Return the longest run after searching for runs at each character.
    return longest_run


main()