from sys import argv
import csv

def main():

    # dict to keep track of how many consecutive copies of each STR is present
    sequenceRepeats = {}

    # Ensuring correct number of Command-line arguments
    if len(argv) != 3:
        print("Usage: python dna.py data.csv. sequence.txt")
        return 1

    # List of STRs to check - depends on which STRs present in database input file
    checkSTRS = []

    # Open the database file first quickly to determine which STRs to search against
    with open(argv[1], "r") as strFile:
        reader = csv.reader(strFile)
        lineCounter = 0
        for line in reader:
            if lineCounter == 0:
                # First Line - get data then stop loop, we have what we need
                # Loop through this line (csv header) and extract the STRs present
                for STR in line:
                    if STR != 'name':
                        checkSTRS.append(STR)
                break
            break

    # go through sequence file and populate sequenceRepeats
    with open(argv[2], "r") as sequenceFile:
        for line in sequenceFile:
            sequence = line

        for strepeat in checkSTRS:
            # check how many consecutive repeats this specific STR has in sequence
            sequenceRepeats[strepeat] = getRepeats(sequence, strepeat)

    # Open the database file once more
    # Then compare each line (i.e. each person) with the sequence
    with open(argv[1], "r") as strFile:
        reader = csv.DictReader(strFile)
        # Set default value for match
        matchedPerson = "No match"

        for line in reader:  # looping through each line i.e. each person
            strsMatched = 0
            # Do this for each STR
            for strepeat in checkSTRS:
                # Loop through each person and compare number of each STR
                if line[strepeat] == str(sequenceRepeats[strepeat]):
                    # Continue = same number for this STR
                    strsMatched += 1

            if strsMatched == len(checkSTRS):
                # Matched on all STRS = this is the person who matches the sequence!
                matchedPerson = line['name']
                break  # no need to continue = we have a match

        # FINALLY - print the matched person
        print(matchedPerson)


# This function takes a sequence and an STR and finds how many times this STR is present consecutively within it
def getRepeats(sequence, strepeat):

    # Get length of str to search for
    strlength = len(strepeat)

    # Loop through sequence, 1 base at a time
    baseCounter = 0  # variable to track progress through sequence
    lastRepeatIndex = 0  # variable to hold index of last repeat location
    conRepeats = 0  # variable to count consecutive repeats
    repeatList = []  # list to hold repeats

    # find consecutive repeats and count them, add these to repeatList and then at the end - return the highest number in this list i.e. the highest number of repeats

    while baseCounter <= len(sequence) - 1:
        # Look at the baseCounter and X bases in front of it - where x is length of     STR to search for
        check = sequence[baseCounter: baseCounter+strlength]
        if check == strepeat:

            # if the last repeat was 1 STR length behind == consecutive
            if lastRepeatIndex == baseCounter - strlength:
                conRepeats += 1

            # Not consecutive and not the first one
            elif lastRepeatIndex != 0:
                # Not consecutive - add current count to countList and reset
                repeatList.append(conRepeats)
                conRepeats = 0

            else:
                # base lastRepeatIndex = 0 - do nothing
                pass

            # Because it is a repeat = update lastRepeatIndex
            lastRepeatIndex = baseCounter
            baseCounter += strlength  # skip STR length along

            # If no previous repeats = set repeats to 1 to include the first repeat
            if conRepeats == 0:
                conRepeats += 1

        else:
            # if not repeat = go to next base
            baseCounter += 1

    # add residual repeats to repeatList
    repeatList.append(conRepeats)

    # Return the largest number of consecutive repeats
    return max(repeatList)


if __name__ == "__main__":
    main()