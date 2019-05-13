import random

# game score
gameScore = 0
# game matrix
matrix = []


# initialize game
def init_matrix():
    global matrix
    matrix = [[0 for i in range(4)] for j in range(4)]


# print number or blank
def init_gameNum(num):
    return num if num != 0 else ' '


# print the game status
def print_game():
    print("The current score is：", gameScore)
    print(""" 
              ┌─────┬─────┬─────┬─────┐
              │%4s │%4s │%4s │%4s │
              ├─────┬─────┬─────┬─────┤
              │%4s │%4s │%4s │%4s │
              ├─────┬─────┬─────┬─────┤
              │%4s │%4s │%4s │%4s │
              ├─────┬─────┬─────┬─────┤
              │%4s │%4s │%4s │%4s │
              └─────┴─────┴─────┴─────┘""" % (
    init_gameNum(matrix[0][0]), init_gameNum(matrix[0][1]), init_gameNum(matrix[0][2]), init_gameNum(matrix[0][3]), \
    init_gameNum(matrix[1][0]), init_gameNum(matrix[1][1]), init_gameNum(matrix[1][2]), init_gameNum(matrix[1][3]), \
    init_gameNum(matrix[2][0]), init_gameNum(matrix[2][1]), init_gameNum(matrix[2][2]), init_gameNum(matrix[2][3]), \
    init_gameNum(matrix[3][0]), init_gameNum(matrix[3][1]), init_gameNum(matrix[3][2]), init_gameNum(matrix[3][3])))


# randomly generate 2 or 4， time means the number of the digit
def getNum2oR4(time=1):
    global matrix
    numSum = 0
    while True:
        num = 2 if random.randrange(0, 20) >= 1 else 4  # the ration of 2 and 4 is 20:1
        index = divmod(random.randrange(0, 16), 4)
        if matrix[index[0]][index[1]] == 0:
            matrix[index[0]][index[1]] = num
            numSum += 1

        if numSum == time:
            break


# check whether the game is over
def check_GG():
    for i in range(0, 4):
        for j in range(0, 3):
            if matrix[i][j] == 0 or matrix[i][j + 1] == 0 or matrix[i][j] == matrix[i][j + 1] or matrix[j][i] == \
                    matrix[j + 1][i]:
                return True
    else:
        return False


# check whether the play can move up.
# If there is no 0 on the upper side of each non-zero number or there is no equal number on the upper side of each non-zero number, the upshift is invalid.
def check_move_up():
    for j in range(0, 4):
        for i in range(1, 4):
            if (matrix[i][j] != 0 and matrix[i - 1][j] == 0) or (
                    matrix[i][j] != 0 and matrix[i][j] == matrix[i - 1][j]):
                return True
    print("can't move up！")
    return False


# move up
def move_up():
    if check_move_up():
        global gameScore

        for column in range(0, 4):
            # Merge the same numbers in this column and calculate the score
            for i in range(0, 3):
                for j in range(i + 1, 4):
                    if matrix[j][column] != 0 and matrix[j][column] != matrix[i][column]:  #avoid to merge two non-adjacent cells
                        break
                    if matrix[j][column] != 0 and matrix[j][column] == matrix[i][column]:
                        matrix[i][column] = matrix[i][column] * 2
                        matrix[j][column] = 0
                        gameScore += matrix[i][column]

                        # If 2048 occurs, the game ends and gives the score of this game.
                        if matrix[i][column] == 2048:
                            print("You win！\n The score is：", gameScore)
                            exit()

                        break

            # Eliminate vacancies of this column
            for j in range(0, 4):
                temp_matrix = [0, 0, 0, 0]
                k = 0
                for i in range(0, 4):
                    if matrix[i][j] != 0:
                        temp_matrix[k] = matrix[i][j]
                        k += 1
                for i in range(0, 4):
                    matrix[i][j] = temp_matrix[i]

        getNum2oR4()

    else:
        pass


# check whether the play can move down.
# If there is no 0 on the under side of each non-zero number or there is no equal number on the under side of each non-zero number, the downshift is invalid.
def check_move_down():
    for j in range(0, 4):
        for i in range(2, -1, -1):
            if (matrix[i][j] != 0 and matrix[i + 1][j] == 0) or (
                    matrix[i][j] != 0 and matrix[i][j] == matrix[i + 1][j]):
                return True
    print("can't move down！")
    return False


# move down
def move_down():
    if check_move_down():
        global gameScore

        for column in range(0, 4):
            # Merge the same numbers in this column and calculate the score
            for i in range(3, 0, -1):
                for j in range(i - 1, -1, -1):
                    if matrix[j][column] != 0 and matrix[j][column] != matrix[i][column]:  #avoid to merge two non-adjacent cells
                        break
                    if matrix[j][column] != 0 and matrix[j][column] == matrix[i][column]:
                        matrix[i][column] = matrix[i][column] * 2
                        matrix[j][column] = 0
                        gameScore += matrix[i][column]

                        # If 2048 occurs, the game ends and gives the score of this game.
                        if matrix[j][column] == 2048:
                            print("You win！\n The score is：", gameScore)
                            exit()

                        break

            # Eliminate vacancies of this column
            for j in range(0, 4):
                temp_matrix = [0, 0, 0, 0]
                k = 3
                for i in range(3, -1, -1):
                    if matrix[i][j] != 0:
                        temp_matrix[k] = matrix[i][j]
                        k += -1
                for i in range(3, -1, -1):
                    matrix[i][j] = temp_matrix[i]

        getNum2oR4()

    else:
        pass


# check whether the play can move left.
# If there is no 0 on the left side of each non-zero number or there is no equal number on the left side of each non-zero number, the leftshift is invalid.
def check_move_left():
    for i in range(0, 4):
        for j in range(1, 4):
            if (matrix[i][j] != 0 and matrix[i][j - 1] == 0) or (
                    matrix[i][j] != 0 and matrix[i][j] == matrix[i][j - 1]):
                return True
    print("can't move left！")
    return False


# move left
def move_left():
    if check_move_left():
        global gameScore

        for row in range(0, 4):
            # Merge the same numbers in this column and calculate the score
            for i in range(0, 3):
                for j in range(i + 1, 4):
                    if matrix[row][j] != 0 and matrix[row][j] != matrix[row][i]:  #avoid to merge two non-adjacent cells  eg：0242 (left)-> 0440
                        break
                    if matrix[row][j] != 0 and matrix[row][j] == matrix[row][i]:
                        matrix[row][i] = matrix[row][i] * 2
                        matrix[row][j] = 0
                        gameScore += matrix[row][i]

                        # If 2048 occurs, the game ends and gives the score of this game.
                        if matrix[row][i] == 2048:
                            print("You win！\n The score is：", gameScore)
                            exit()

                        break

            # Eliminate vacancies of this row
            for i in range(0, 4):
                temp_matrix = [0, 0, 0, 0]
                k = 0
                for j in range(0, 4):
                    if matrix[i][j] != 0:
                        temp_matrix[k] = matrix[i][j]
                        k += 1
                for j in range(0, 4):
                    matrix[i][j] = temp_matrix[j]
        getNum2oR4()

    else:
        pass


# check whether the play can move right.
# If there is no 0 on the right side of each non-zero number or there is no equal number on the right side of each non-zero number, the rightshift is invalid.

def check_move_right():
    for i in range(0, 4):
        for j in range(2, -1, -1):
            if (matrix[i][j] != 0 and matrix[i][j + 1] == 0) or (
                    matrix[i][j] != 0 and matrix[i][j] == matrix[i][j + 1]):
                return True
    print("can't move right！")
    return False


# move right
def move_right():
    if check_move_right():
        global gameScore

        for row in range(0, 4):
            # Merge the same numbers in this column and calculate the score
            for i in range(3, 0, -1):
                for j in range(i - 1, -1, -1):
                    if matrix[row][j] != 0 and matrix[row][j] != matrix[row][i]: #avoid to merge two non-adjacent cells
                        break
                    if matrix[row][j] != 0 and matrix[row][j] == matrix[row][i]:
                        matrix[row][i] = matrix[row][i] * 2
                        matrix[row][j] = 0
                        gameScore += matrix[row][i]

                        # If 2048 occurs, the game ends and gives the score of this game.
                        if matrix[row][i] == 2048:
                            print("You win！\n The score is：", gameScore)
                            exit()

                        break

            # Eliminate vacancies of this row
            for i in range(3, -1, -1):
                temp_matrix = [0, 0, 0, 0]
                k = 3
                for j in range(3, -1, -1):
                    if matrix[i][j] != 0:
                        temp_matrix[k] = matrix[i][j]
                        k += -1
                for j in range(3, -1, -1):
                    matrix[i][j] = temp_matrix[j]
        getNum2oR4()

    else:
        pass


# main function
def main():
    global gameScore

    init_matrix()
    getNum2oR4(2)
    print_game()
    direction = input("(↑:w) (↓:s) (←:a) (→:d) (restart:r)")

    # game won't end until there is no step to move or 2048 appears
    while True:

        # up
        if direction == 'w':
            move_up()

        # down
        elif direction == 's':
            move_down()

        # left
        elif direction == 'a':
            move_left()

        # right
        elif direction == 'd':
            move_right()

        # restart
        elif direction == 'r':
            init_matrix()
            getNum2oR4(2)
            gameScore = 0

        # other cases
        else:
            print("invalid input！")

        print_game()

        if not check_GG():
            print("Game Over\nScore : ", gameScore)
            break

        direction = input("(↑:w) (↓:s) (←:a) (→:d) (restart:r)")


if __name__ == '__main__':
    main()

