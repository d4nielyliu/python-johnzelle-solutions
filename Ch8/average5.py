
def main():
    fileName = input("Please enter the file name? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", sum / count)

main()
