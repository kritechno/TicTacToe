import random

a = (9 * " ")
M = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]


def field():
    print("---------")
    print("| " + " ".join(M[0]) + " |")
    print("| " + " ".join(M[1]) + " |")
    print("| " + " ".join(M[2]) + " |")
    print("---------")


def win():
    if len(set(M[0])) <= 1 and M[0][0] != " ":
        print("{0} wins!".format(M[0][0]))
        return True
    elif len(set(M[1])) <= 1 and M[1][0] != " ":
        print("{0} wins!".format(M[1][0]))
        return True
    elif len(set(M[2])) <= 1 and M[2][0] != " ":
        print("{0} wins!".format(M[2][0]))
        return True
    elif M[0][0] == M[1][0] == M[2][0] and M[0][0] != " ":
        print("{0} wins!".format(M[0][0]))
        return True
    elif M[1][1] == M[1][2] == M[1][0] and M[1][0] != " ":
        print("{0} wins!".format(M[1][0]))
        return True
    elif M[2][1] == M[2][2] == M[2][0] and M[2][0] != " ":
        print("{0} wins!".format(M[2][0]))
        return True
    elif M[0][0] == M[1][1] == M[2][2] and M[0][0] != " ":
        print("{0} wins!".format(M[0][0]))
        return True
    elif M[0][2] == M[1][1] == M[2][0] and M[2][0] != " ":
        print("{0} wins!".format(M[2][0]))
        return True
    else:
        return False


t = 0
field()
while True:
    c = input("Enter coordinates: ")
    if c[0].isnumeric() and c[2].isnumeric():
        el1 = (int(c[0]) - 1)
        el2 = (int(c[2]) - 1)
        if int(c[0]) > 3 or int(c[2]) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if " " not in M[el1][el2]:
                print("This cell is occupied! Choose another one!")
            else:
                if M[el1][el2] == " " and (el1 <= 3 or el2 <= 3):
                    t += 1
                    M[el1][el2] = "X"
                    field()
                    win()
                    if t == 9 and win() is False:
                        print("Draw!")
                        break
                    if win() is True:
                        break
    else:
        print("You should enter numbers!")
    c1 = random.randint(0, 3)
    c2 = random.randint(0, 3)
    c = ("{0} {1})".format(c1, c2))
    if c[0].isnumeric() and c[2].isnumeric():
        el1 = (int(c[0]) - 1)
        el2 = (int(c[2]) - 1)
        if int(c[0]) > 3 or int(c[2]) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if " " not in M[el1][el2]:
                print("This cell is occupied! Choose another one!")
            else:
                if M[el1][el2] == " " and (el1 <= 3 or el2 <= 3):
                    t += 1
                    M[el1][el2] = "O"
                    field()
                    win()
                    if t == 9 and win() is False:
                        print("Draw!")
                        break
                    if win() is True:
                        break
    else:
        print("You should enter numbers!")
