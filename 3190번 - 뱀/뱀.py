#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/10/16 17:03:45 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 사과 -> 머리+1 
# not 사과 -> 꼬리+1, 머리+1
# 몇초에 끝나는가
# 벽 혹은 몸에 부딪히면 끝남

import sys
from collections import deque

# 1. 입력받기
n = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)]

k = int(sys.stdin.readline())
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1

l = int(sys.stdin.readline())

direction = deque()
for i in range(l):
    t, d = sys.stdin.readline().split()
    direction.append((int(t), d))

# 2. 초기 상태 설정
# 동 서 남 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0 # 뱀 머리
board[x][y] = 2
time = 0
snake = deque([(0, 0)])

# 3. 게임 시작
while True:
    time += 1
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    # 중단조건
    if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        break
    
    # 사과 있을 때
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        tx, ty = snake.popleft()
        board[tx][ty] = 0
    
    x, y = nx, ny
    board[x][y] = 2
    snake.append((x, y))
    
    if direction and time == direction[0][0]:
        t, d = direction.popleft()
        if d == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4

print(time)
        
    
    
    
 
   
       
   