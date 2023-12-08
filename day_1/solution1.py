def firstD(line):
    digit = ""
    for element in range(0, len(line)):
        if line[element].isdigit():
            digit = line[element]
            return digit
def lastD(line):
    digit = ""
    for element in range(-1, len(line)):
        if line[element].isdigit():
            digit = line[element]
    return digit

def calibrationSum(filename):    
    calibrationValues = open(filename,'r')
    lines = calibrationValues.readlines()
    sum = 0
    for line in lines:
        firstDigit = firstD(line)
        lastDigit = lastD(line)
        numberAsString = firstDigit+lastDigit
        sum += int(numberAsString)
        print(numberAsString)
    return sum

if __name__ == "__main__":
    result=calibrationSum('.personal_input.txt')
    print(result)