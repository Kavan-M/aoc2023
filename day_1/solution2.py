numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversedNumbers = [i[::-1] for i in numbers]
def firstD(line):
    digit = ""
    
    for element in range(0, len(line)):
        if line[element].isdigit():
            digit = line[element]
            return digit
            break
        num = 1
        for number in numbers:
            if line.find(number,element,element+len(number))!=-1:
                digit = str(num)
                return digit
                break
            num+=1


def lastD(line):
    digit = ""
    line = line[::-1]    
    for element in range(0, len(line)):
        if line[element].isdigit():
            digit = line[element]
            return digit
            break
        num = 1
        for number in reversedNumbers:
            if line.find(number,element,element+len(number))!=-1:
                digit = str(num)
                return digit
                break
            num+=1

def calibrationSum(filename):    
    calibrationValues = open(filename,'r')
    lines = calibrationValues.readlines()
    sum = 0
    for line in lines:
        firstDigit = firstD(line)
        lastDigit = lastD(line)
        numberAsString = str(firstDigit)+lastDigit
        sum += int(numberAsString)
        print(numberAsString)
    return sum

if __name__ == "__main__":
    result=calibrationSum('.personal_input.txt')
    print(result)

