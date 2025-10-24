#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1520                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1520                           #+#        #+#      #+#     #
#    Solved: 2025/10/24 13:58:07 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(10**6)

m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 방문 좌표
dp = [[-1 for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 경우의 수 -> dfs
def dfs(x, y):
    # 목적지에 도착하면 return
    if x == m -1 and y == n -1:
        return 1
    
    # 메모이제이션: 이미 방문한 곳이면 저장된 값 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문한 적 없다면 dfs
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 경로의 수 누적
        if 0 <= nx < m and 0 <= ny < n and board[x][y] > board[nx][ny]:
            dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]

print(dfs(0, 0))