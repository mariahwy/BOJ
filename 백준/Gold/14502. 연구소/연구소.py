#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2025/10/27 14:35:40 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations 
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def bfs(sim_map, sim_virus_q):
    infected_cnt = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while sim_virus_q:
        (cx, cy) = sim_virus_q.popleft()
            
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and sim_map[nx][ny] == 0:
                sim_map[nx][ny] = 2
                sim_virus_q.append((nx, ny))
                infected_cnt += 1  
                
    return infected_cnt

# 1. 바이러스, 빈칸 위치 확인
virus = deque()
empty = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            empty.append((i, j))
            
# 2. 랜덤으로 벽 3개 세우기 (3개 뽑기)
wall_comb = combinations(empty, 3)
max_safe_area = 0
initial_empty_cnt = len(empty)

for wall_set in wall_comb:
    # 시뮬레이션용 맵 복사
    sim_map = copy.deepcopy(board)
    sim_virus_q = virus.copy()
    
    # 벽 세우기
    for (wx, wy) in wall_set:
        sim_map[wx][wy] = 1
        
    # 바이러스 전파
    infected_cnt = bfs(sim_map, sim_virus_q)

    curr_safe_area = initial_empty_cnt - 3 - infected_cnt
                
    # 최대 안전영역 갱신
    if curr_safe_area > max_safe_area:
        max_safe_area = curr_safe_area       
                
print(max_safe_area)