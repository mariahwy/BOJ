#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2025/10/24 10:58:13 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())

board = []
for j in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

directions = list(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move_east():
    temp = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = dice[2]
    dice[2] = temp

def move_west():
    temp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = temp
    
def move_north():
    temp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = temp
    
def move_south():
    temp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = temp

def change_board(cx, cy):
    if board[cx][cy] == 0:
        board[cx][cy] = dice[5]
    else:
        dice[5] = board[cx][cy]
        board[cx][cy] = 0

cx = x
cy = y
for d in directions:
    nx = cx + dx[d-1]
    ny = cy + dy[d-1]
    
    # 범위 체크
    if 0 <= nx < n and 0 <= ny < m:
        cx = nx
        cy = ny
        
        if d == 1:
            move_east()
            change_board(cx, cy)
        elif d == 2:
            move_west()
            change_board(cx, cy)
        elif d == 3:
            move_north()
            change_board(cx, cy)
        else:
            move_south()
            change_board(cx, cy)
        
        print(dice[0])
        
    else:
        continue
    