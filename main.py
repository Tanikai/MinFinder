from timeit import default_timer as timer
import datetime
import csv

from MinFinder import MinFinder
import NumberFactory

TESTLENGTHS = [10, 100, 1000, 2000, 4000, 8000]

def StartMinFinderTests():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    WriteResultLine([timestamp, "5 iterations per array length"])
    runs = 5
    WriteResultLine(["~"*15])

    for l in TESTLENGTHS:
        print("Starting measurement for length " + str(l) + " with random array...")
        avgTime = MeasureMinFinder(NumberFactory.GetUnsortedSet, l, runs)
        print("Average time needed with {0} elements: {1} s ({2} runs)".format(l, avgTime, runs))
        WriteResultLine(["random", runs, l, avgTime])
    WriteResultLine(["~"*15])

    for l in TESTLENGTHS:
        print("Starting measurement for length " + str(l) + " with sorted array...")
        avgTime = MeasureMinFinder(NumberFactory.GetSortedSet, l, runs)
        print("Average time needed with {0} elements: {1} s ({2} runs)".format(l, avgTime, runs))
        WriteResultLine(["sorted", runs, l, avgTime])
    WriteResultLine(["~"*15])

    for l in TESTLENGTHS:
        print("Starting measurement for length " + str(l) + " with reverse sorted array...")
        avgTime = MeasureMinFinder(NumberFactory.GetReverseSortedSet, l, runs)
        print("Average time needed with {0} elements: {1} s ({2} runs)".format(l, avgTime, runs))
        WriteResultLine(["reverse sorted", runs, l, avgTime])
    WriteResultLine(["~"*15])

    WriteResultLine(["-"*30])

def MeasureMinFinder(arrayGenerator, arrayLength, runCount):
    timesum = 0
    for i in range(runCount):
        arr = arrayGenerator(arrayLength)
        start = timer()
        sortedArray = MinFinder(arr)
        end = timer()
        timesum += (end-start)
    return (timesum / runCount)

def WriteResultLine(line):
    with open("results.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(line)

if __name__ == "__main__":
    StartMinFinderTests()
