def main():
    x = input(eval("Please report speed: "))
    y = input(eval("What is the reported speed limit?"))

    d = x - y
    if d >= 0:
        fine = (d // 5) * 5 + 50
        if x >= 90:
            fine = fine + 200
        print("You owe ${0}.".format(fine))
    elif d < 0:
        print("You have not committed a speed violation.")
    else:
        print("Check the speed limit or reported speed.")
main()
