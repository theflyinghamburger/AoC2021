class SubPos:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def forward(self, dist):
        self.x += dist

    def forward_aim(self, dist):
        self.x += dist
        self.y += self.aim * dist

    def down(self, dist):
        self.y += dist

    def down_aim(self, dist):
        self.aim += dist

    def up(self, dist):
        self.y -= dist

    def up_aim(self, dist):
        self.aim -= dist


class SubCommand:
    def __init__(self, type_, dist_):
        self.type = type_
        self.dist = dist_
        # print(self.type, self.dist)


def read_input(filename):
    inputFile = open(filename, "r")
    inputArr = []
    for line in inputFile:
        temp = SubCommand((line.strip()).split()[0], int((line.strip()).split()[1]))
        inputArr.append(temp)
    inputFile.close()
    # print(inputArr)  # value format check
    return inputArr


def soln1(inputList_, subPos_):
    # Solution for part 1

    for command in inputList_:
        if command.type == "forward":
            subPos_.forward(command.dist)
        elif command.type == "up":
            subPos_.up(command.dist)
        elif command.type == "down":
            subPos_.down(command.dist)

    return subPos_.x * subPos_.y


def soln2(inputList_, subPos_):
    # Solution for part 1
    for command in inputList_:
        if command.type == "forward":
            subPos_.forward_aim(command.dist)
        elif command.type == "up":
            subPos_.up_aim(command.dist)
        elif command.type == "down":
            subPos_.down_aim(command.dist)

    return subPos_.x * subPos_.y


if __name__ == "__main__":
    subPos = SubPos()
    inputList = read_input("input.txt")
    sizeOfInputList = len(inputList)
    print(sizeOfInputList)  # Sanity check

    solution1 = soln1(inputList, subPos)

    subPos.x = 0  # reset sub position
    subPos.y = 0

    solution2 = soln2(inputList, subPos)
    print("Final horizontal * depth = ", solution1)  # Subtract 1 to match problem example
    print("Final horizontal * depth with aim = ", solution2)  # Subtract 1 to match problem example
