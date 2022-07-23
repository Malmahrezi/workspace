from sys import argv
import csv

def main():
    sequenceRepeats = {}
    if len(argv) != 3:
        print("Usage: python dna.py data.csv. sequence.txt")
        return 1
    checkSTRS = []
    with open(argv[1], "r") as strFile:
        reader = csv.reader(strFile)
        lineCounter = 0
        for line in reader:
            if lineCounter == 0:
                for STR in line:
                    if STR != 'name':
                        checkSTRS.append(STR)
                break
            break
    with open(argv[2], "r") as sequenceFile:
        for line in sequenceFile:
            sequence = line
        for strepeat in checkSTRS:
            sequenceRepeats[strepeat] = getRepeats(sequence, strepeat)
    with open(argv[1], "r") as strFile:
        reader = csv.DictReader(strFile)
        matchedPerson = "No match"
        for line in reader:
            strsMatched = 0
            for strepeat in checkSTRS:
                if line[strepeat] == str(sequenceRepeats[strepeat]):
                    strsMatched += 1
            if strsMatched == len(checkSTRS):
                matchedPerson = line['name']
                break
        print(matchedPerson)
def getRepeats(sequence, strepeat):
    strlength = len(strepeat)
    baseCounter = 0
    lastRepeatIndex = 0
    conRepeats = 0
    repeatList = []
    while baseCounter <= len(sequence) - 1:
        # Look at the baseCounter and X bases in front of it - where x is length of     STR to search for
        check = sequence[baseCounter: baseCounter+strlength]
        if check == strepeat:
            if lastRepeatIndex == baseCounter - strlength:
                conRepeats += 1
            elif lastRepeatIndex != 0:
                repeatList.append(conRepeats)
                conRepeats = 0
            else:
                pass
            lastRepeatIndex = baseCounter
            baseCounter += strlength
            if conRepeats == 0:
                conRepeats += 1
        else:
            baseCounter += 1
    repeatList.append(conRepeats)
    return max(repeatList)
if __name__ == "__main__":
    main()