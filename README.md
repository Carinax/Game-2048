# Game-2048
IS 452 final

To start the game, run:

python game2048.py/python3 game2048.py

# Rules:

The rule of this game is simple. It’s a 4*4 board, at first, two numbers (only 2 or 4) randomly appear on this board, players can choose 4 different directions which are up, down, right and left. If the numbers in the board appear to shift or merge, they will be deemed as effective move. If the player chooses the same number in the direction of the merger, each effective move can be merged at the same time, but not consecutive merger. All the newly generated numbers from the merge add to the valid score for that step. For each valid move, a random number (which could still be 2 or 4) appears in the chessboard's empty space. If the board is full of numbers, unable to move effectively, game over. If 2048 appears on the board, the player wins and the game is over. In addition, score will be calculated for every effective move. For example, if two “4”be added for this move, we will get a “8”and the score will be added 8. As a result, in a competition, if two competitors both fail to get 2048, we can compare their score and get to know who wins.

# How to play
W⬆️ S⬇️ A⬅️ D➡️
