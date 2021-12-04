def read_input(filename):
    inputFile = open(filename, "r")
    inputArr = []
    for line in inputFile:
        inputArr.append(int(line.strip()))
    inputFile.close()
    # print(inputArr)  # value format check
    return inputArr


def soln1():
    # Solution for part 1
    incDepthCnt = 0
    prevDepth = 0
    for index, elem in enumerate(inputList):
        if elem > prevDepth:
            incDepthCnt += 1
        prevDepth = elem
    return incDepthCnt


def soln2():
    # Solution for part 2
    prevSum3 = 0
    incDepthCntSum = 0
    for index, elem in enumerate(inputList):
        if (index + 2) < sizeOfInputList:
            newSum3 = inputList[index] + inputList[index + 1] + inputList[index + 2]
            if newSum3 > prevSum3:
                incDepthCntSum += 1
            prevSum3 = newSum3
        else:
            break
    return incDepthCntSum


if __name__ == "__main__":
    inputList = read_input("input.txt")
    sizeOfInputList = len(inputList)
    # print(sizeOfInputList)  # Sanity check

    solution1 = soln1()
    solution2 = soln2()
    print("Final depth increments = ", solution1 - 1)  # Subtract 1 to match problem example
    print("Final sum depth increments = ", solution2 - 1)  # Subtract 1 to match problem example
