def MinFinder(A):
    # initialize variables
    L = len(A)-1
    NextIterPoint = 0
    PositionOfMinValue = 0

    sorted = False
    while (not sorted):
        minValue = A[PositionOfMinValue]
        for i in range(PositionOfMinValue+1, L+1):
            if (minValue > A[i]):
                minValue = A[i]
                PositionOfMinValue = i
                if (i != L):
                    break

            if (i == L):
                for j in range(PositionOfMinValue, NextIterPoint, -1):
                    A[j] = A[j-1]
                A[NextIterPoint] = minValue
                NextIterPoint += 1
                PositionOfMinValue = NextIterPoint
                break

        if (not (PositionOfMinValue < L)):
            sorted = True
    return A
