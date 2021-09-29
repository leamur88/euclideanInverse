import math


class NoInverseExists(Exception):
    pass


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def find_mod(x, n):
    multipliers = []
    i = 0
    try:
        while x != 0:
            temp = x
            multipliers.append(math.floor(n / x))
            x = (n % x)
            print("Step ", i, ": ", n, " = ", multipliers[i], "(", temp, ")", " + ", x, sep='')
            n = temp
            i += 1
        if n != 1:
            raise NoInverseExists()
        else:
            return multipliers
    except NoInverseExists:
        print("This equation has no inverse")


def find_inverse(mult, n):
    auxillary = [0, 1]
    step = 0
    print("p", step, " = ", auxillary[step], sep='')
    step += 1
    print("p", step, " = ", auxillary[step], sep='')
    i = 0
    while i < len(mult) - 1:
        step += 1
        subtraction = auxillary[step - 2] - auxillary[step - 1] * mult[i]
        modulo = subtraction % n
        print("p", step, " = (", auxillary[step - 2], " - ", auxillary[step - 1], "(", mult[i], ")) % ", n, " = ",
              modulo, sep='')
        auxillary.append(modulo)
        i += 1
    return auxillary[-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = "nope"
    while 1:
        x = int(input("Please input the number you want to find the inverse for: "))
        n = int(input("Please input the number you want mod by: "))
        print("You would like to find the inverse of ", x, " mod ", n, "? [y/n] ", sep='', end='')
        response = input()
        if response == "y" or response == "yes":
            mult = find_mod(x, n)
            inverse = find_inverse(mult, n)
            if (x * inverse) % n == 1:
                print("The inverse is: ", inverse, "!!!!", sep='')
                print("This means that ", x, "(", inverse, ") % ", n, " = 1", sep='')
                break
            else:
                print("Inverse unfortunately could not be calculated...")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
