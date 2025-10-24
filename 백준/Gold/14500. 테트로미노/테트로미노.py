#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2025/10/24 12:45:50 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

n, m  = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def first():
    cnt = 0
    for i in range(n):
        for j in range(0, m-3):
            cnt = max(cnt, board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3])
            
    for j in range(m):
        for i in range(0, n-3):
            cnt = max(cnt, board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j])
    return cnt

def second():
    cnt = 0
    for i in range(0, n-1):
        for j in range(0, m-1):
            cnt = max(cnt, board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1])
    return cnt

def third():
    cnt = 0
    for i in range(0, n-1):
        for j in range(0, m-2):
            cnt = max(cnt,
                      board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j],
                      board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1],
                      board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2],
                      board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j],
                      board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+1],
                      board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+2],
                      # Z모양
                      board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2],
                      board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1]
                    )
    for j in range(0, m-1):
        for i in range(0, n-2):
            cnt = max(cnt,
                      board[i][j] + board[i+1][j] + board[i+2][j] + board[i][j+1],
                      board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j+1],
                      board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1],
                      board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i][j],
                      board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+1][j],
                      board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j],
                      # z모양
                      board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1],
                      board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
                    )
    return cnt

a = first()
b = second()
c = third()
print(max(a,b,c))
