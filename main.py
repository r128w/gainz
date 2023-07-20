import sys

# format:
# [date DD-MM-YYYY]|[focus]|[exercise 1]|[exercise 2]etc
# exercise format:
# 1. sets of reps: |[sets]x[reps]-[name]-[rest (seconds)]-[weight(optional)]|
# 2. decreasing: |[reps]v[decrease]-[name]-[rest]-[weight(optional)]|
# 3. 

def openFile(FIQ):
    file = open(FIQ,"r")
    lines = []
    for x in file:# initializes lines as a list of all lines
        lines.append(x)
    for i in range(len(lines)):# gets rid of \n at the end of all lines
        if i != len(lines)-1:
            lines[i] = lines[i][:-1]
    return lines

def parseLine(line):
    return line.split("|")# ID 0: date, ID 1: focus, ID 2-inf: exercises

def displayWO(WIQ):#WO in question
    nameDate = WIQ[0] + ": " + WIQ[1]
    print("-=- " + nameDate)
    for i in range(len(WIQ)-2):
        print("      " + WIQ[i+2].replace("-", " "))

archiveLines = openFile("gainz\\archive.txt")
if sys.argv[1] == "show":
    for i in range(len(archiveLines)):
        displayWO(parseLine(archiveLines[i]))

if sys.argv[1] == "add" :
    newDate = input("enter date ? ")
    newFocus = input("focus ? ")
    newEntry = newDate + "|" + newFocus
    exerciseCount = int(input("exercises ? "))
    for i in range(exerciseCount):
        print("Exercise " + str(i+1) + ":")
        newEntry += "|" + input("  sets ? ") + "x" + input("  reps ? ") + "-" + input("  name ? ") + "-" + input("  rest ? ")
        if input("  weight (y/n) ? ") == "y":
            newEntry += "-" + input("  amount ? ")
    FTW = "" # File To Write
    for line in archiveLines:
        FTW += line + "\n"
    FTW+=newEntry

    archive = open("gainz\\archive.txt", "w")
    archive.write(FTW)

if sys.argv[1] == "type":
    for i in range(len(archiveLines)):
        parsedLine = parseLine(archiveLines[i])
        print(parsedLine[0] + ": " + parsedLine[1])