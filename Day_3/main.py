bitFrameLength = 12
class BitFrame:  #
    def __init__(self):
        self.bits = []
        self.len = 12

    def update(self, val):
        for a in range(self.len):
            self.bits.append((val >> a) & 1)
        self.bits.reverse()
        return self.bits

class TotalDiag:
    def __init__(self):
        self.epsilon = 0
        self.gamma = 0
        self.window = []
        self.windowO2 = []
        self.windowCO2 = []
        self.CO2 = 0
        self.O2 = 0
        self.zeroCount = [0] * bitFrameLength
        self.oneCount = [0] * bitFrameLength

    def add_to_window(self, bit_frame):
        self.window.append(bit_frame)

    def populate_bit_counts(self):
        for bit_frame in self.window:
            for index, bit_ in enumerate(bit_frame.bits):
                if bit_ == 1:
                    self.oneCount[index] += 1
                else:
                    self.zeroCount[index] += 1

    def find_epsilon_gamma(self):

        epsi_list = [0] * bitFrameLength
        gamma_list = [0] * bitFrameLength

        for index, bit_ in enumerate(epsi_list):
            if self.oneCount[index] >= self.zeroCount[index]:
                epsi_list[index] = 1
                gamma_list[index] = 0
            else:
                epsi_list[index] = 0
                gamma_list[index] = 1

            self.epsilon += epsi_list[index] << (bitFrameLength - index - 1)
            self.gamma += gamma_list[index] << (bitFrameLength - index - 1)

        return self.epsilon, self.gamma

    def prepare_O2_CO2_windows(self):
        self.windowO2 = self.window
        self.windowCO2 = self.window
        length_CO2 = len(self.windowCO2)

        while len(self.windowO2) > 1:
            for index in range(bitFrameLength):
                if self.oneCount[index] >= self.zeroCount[index]:
                    #print("OneCount >= ZeroCount")
                    self.windowO2 = [x for x in self.windowO2 if x.bits[index] == 1]

                    if length_CO2 > 1:
                        self.windowCO2 = [x for x in self.windowCO2 if x.bits[index] == 0]
                        length_CO2 = len(self.windowCO2)
                else:
                    #print("OneCount < ZeroCount")
                    self.windowO2 = [x for x in self.windowO2 if x.bits[index] == 0]

                    if length_CO2 > 1:
                        self.windowCO2 = [x for x in self.windowCO2 if x.bits[index] == 1]
                        length_CO2 = len(self.windowCO2)

        for index in range(bitFrameLength):
            self.O2 += self.windowO2[0].bits[index] << (bitFrameLength - index - 1)
            self.CO2 += self.windowCO2[0].bits[index] << (bitFrameLength - index - 1)

        return self.O2, self.CO2


def read_input(filename):
    inputFile = open(filename, "r")
    inputArr = []
    for line in inputFile:
        inputArr.append(int(line.strip(), 2))
    inputFile.close()
    return inputArr


def initialise_counts(inputList_, info_):
    for frame in inputList_:
        temp = BitFrame()
        temp.update(frame)
        info_.add_to_window(temp)
    info_.populate_bit_counts()


def soln1(info_):
    # Solution for part 1

    return info_.find_epsilon_gamma()


def soln2(info_):
    # Solution for part 2
    return info_.prepare_O2_CO2_windows()


if __name__ == "__main__":
    inputList = read_input("input.txt")
    sizeOfInputList = len(inputList)
    print(sizeOfInputList)  # Sanity check
    infoDiag = TotalDiag()

    initialise_counts(inputList, infoDiag)

    Epsilon, Gamma = soln1(infoDiag)
    print("Epsilon =", Epsilon)
    print("Gamma = ", Gamma)
    print("Power =", Epsilon * Gamma)

    print(infoDiag.oneCount)
    print(infoDiag.zeroCount)

    O2, CO2 = soln2(infoDiag)
    print("O2 =", O2)
    print("CO2 = ", CO2)
    print("Safety =", O2 * CO2)
