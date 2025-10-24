#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12100                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12100                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 16:26:46 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import copy

n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0

def left(board):
    for i in range(n):
        cur = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
            
                if board[i][cur] == 0:
                    board[i][cur] = tmp
                elif board[i][cur] == tmp:
                    board[i][cur] *= 2
                    cur += 1
                else:
                    cur += 1
                    board[i][cur] = tmp
    return board


def right(board):
    for i in range(n):
        cur = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
            
                if board[i][cur] == 0:
                    board[i][cur] = tmp
                elif board[i][cur] == tmp:
                    board[i][cur] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[i][cur] = tmp
    return board


def up(board):
    for j in range(n):
        cur = 0
        for i in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
            
                if board[cur][j] == 0:
                    board[cur][j] = tmp
                elif board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur += 1
                else:
                    cur += 1
                    board[cur][j] = tmp
    return board


def down(board):
    for j in range(n):
        cur = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
            
                if board[cur][j] == 0:
                    board[cur][j] = tmp
                elif board[cur][j] == tmp:
                    board[cur][j] *= 2
                    cur -= 1
                else:
                    cur -= 1
                    board[cur][j] = tmp
    return board



# 모든 가능한 경우의 수 -> dfs 
# 백트래킹 
def dfs(cnt, board):
    global ans   
    
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                    ans = max(ans, board[i][j])
        return
    
    for i in range(4):
        copy_board = copy.deepcopy(board)
        if i == 0:
            dfs(cnt + 1, left(copy_board))
        elif i == 1:
            dfs(cnt + 1, right(copy_board))
        elif i == 2:
            dfs(cnt + 1, up(copy_board))
        else:
            dfs(cnt + 1, down(copy_board))

dfs(0, board)        
print(ans)