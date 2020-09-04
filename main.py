import csv
from timeit import default_timer as timer
import datetime
import NumberFactory
from MinFinder import MinFinder

TESTLENGTHS = [10, 100, 1000, 10000, 100000]

def StartMinFinderTests():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    WriteResultLine([timestamp])

    for l in TESTLENGTHS:
        MeasureMinFinder(l, 2)

    WriteResultLine(["-"*30])


def MeasureMinFinder(arrayLength, runCount):
    print("Starting measurement for length " + str(arrayLength) + "...")
    timesum = 0
    
    for i in range(runCount):
        print("run " + str(i+1), end = "...")
        unsortedArray = NumberFactory.GetUnsortedSet(arrayLength)
        start = timer()
        sortedArray = MinFinder(unsortedArray)
        end = timer()
        timesum += (end-start) # add current iteration to sum
    print("")

    average = timesum / runCount
    print("Average time needed for {0} iterations with length {1}: {2}".format(10, arrayLength, average))
    print("-"*30)
    WriteResultLine([arrayLength, average])
    

def WriteResultLine(line):
    with open("results.csv", "a+", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(line)

if __name__ == "__main__":
    StartMinFinderTests()