a = input()
b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def caesar(a):
    d = ""
    a = a.upper()
    for i in range(len(a)):
        if a[i] == "X":
            d = d + a[i].replace(a[i], "A")
        elif a[i] == "Y":
            d = d + a[i].replace(a[i], "B")
        elif a[i] == "Z":
            d = d + a[i].replace(a[i], "C")
        elif a[i] == " ":
            d = d + a[i].replace(a[i], " ")
        elif not a[i].isalpha():
            d = d + a[i]
        else:
            d = d + a[i].replace(a[i], b[b.index(a[i])+3])
    return d


def decode(a):
    d = ""
    a = a.upper()
    for i in range(len(a)):
        if a[i] == "A":
            d = d + a[i].replace(a[i], "X")
        elif a[i] == "B":
            d = d + a[i].replace(a[i], "Y")
        elif a[i] == "C":
            d = d + a[i].replace(a[i], "Z")
        elif a[i] == " ":
            d = d + a[i].replace(a[i], " ")
        elif not a[i].isalpha():
            d = d + a[i]
        else:
            d = d + a[i].replace(a[i], b[b.index(a[i])-3])
    return d