# Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

# chessboard(3)
# print()
# chessboard(6)
# Sample output
# 101
# 010
# 101

# 101010
# 010101
# 101010
# 010101
# 101010
# 010101


def chessboard(length):
    for i in range(length):
        output = ""
        for j in range(length):
            if (i + j) % 2 == 0:
                output += "1"
            else:
                output += "0"
        print(output)
