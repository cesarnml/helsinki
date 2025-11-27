# Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

# squared("ab", 3)
# print()
# squared("aybabtu", 5)
# Sample output
# aba
# bab
# aba

# aybab
# tuayb
# abtua
# ybabt
# uayba


def squared(text, length):
    for i in range(length):
        output = ""
        for j in range(length):
            index = (i * length + j) % len(text)
            output += text[index]
        print(output)
