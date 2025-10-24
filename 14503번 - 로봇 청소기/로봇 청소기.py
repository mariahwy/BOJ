#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 13:22:30 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# import sys


# def clean(mat, r, c, cnt):
#     if mat[r][c] == 0:
#         mat[r][c] = -1
#         cnt += 1
#         return 1
#     else:
#         return 0
    
    
# def check_not_cleaned(mat, n, m, r, c):
#     # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
#     if r == 0:
#         if c == 0:
#             if mat[r+1][c] != 0 and mat[r][c+1] != 0:
#                 return 0
#             else:
#                 return 1
                
#         elif c == m-1:
#             if mat[r][c-1] != 0 and mat[r+1][c] != 0:
#                 return 0
#             else:
#                 return 1
    
#         else: 
#             if mat[r][c-1] != 0 and mat[r][c+1] != 0 and mat[r+1][c] != 0:
#                 return 0
#             else:
#                 return 1
            
#     elif r > 0 and r < n-1:
#         if c == 0:
#             if mat[r-1][c] != 0 and mat[r+1][c] != 0 and mat[r][c+1] != 0:
#                 return 0
#             else:
#                 return 1
            
#         elif c == m-1:
#             if mat[r][c-1] != 0 and mat[r-1][c] != 0 and [r+1][c] != 0:
#                 return 0
#             else:
#                 return 1
                
#         else:
#             if mat[r-1][c] != 0 and mat[r][c-1] != 0 and mat[r+1][c] != 1 and mat[r][c+1] != 1:
#                 return 0
#             else:
#                 return 1
            
#     else:
#         if c == 0:
#             if mat[r-1][c] != 0 and mat[r][c+1] != 0:
#                 return 0
#             else: return 1
        
#         elif c == m-1:
#             if mat[r][c-1] != 0 and mat[r-1][c] != 0:
#                 return 0
#             else:
#                 return 1
        
#         else:
#             if mat[r][c-1] != 0 and mat[r][c+1] != 0 and mat[r-1][c] != 0:
#                 return 0
#             else:
#                 return 1
        
        
# def check_back(mat, r, c, d):
#     if d == 0:  # 북
#         if mat[r+1][c] != 1:
#             r += 1
#             return 0
#         else:
#             return -1
    
#     elif d == 1:    # 동
#         if mat[r][c-1] != 1:
#             c -= 1
#             return 0
#         else:
#             return -1
            
#     elif d == 2:    # 남
#         if mat[r-1][c] != 1:
#             r -= 1
#             return 0
#         else:
#             return -1
#     else:   # 서
#         if mat[r][c+1] != 1:
#             c += 1
#             return 0
#         else:
#             return -1
        

# def rotate(d):
#     # 반시계 회전
#     if d == 0:
#         d = 3
#     else:
#         d -= 1
        

# def check_front(mat, r, c, d):
#     if d == 0 : #북
#         if mat[r-1][c] == 0:
#             r -= 1
    
#     elif d == 1:    #동
#         if mat[r][c+1] == 0:
#             c += 1
            
#     elif d == 2:    # 남
#         if mat[r+1][c] == 0:
#             r += 1
            
#     else:   #서
#         if mat[r][c-1] == 0:
#             c -= 1
        

# def main():
#     # 초기 설정
#     n, m = map(int, sys.stdin.readline().split())
#     r, c, d = map(int, sys.stdin.readline().split())

#     mat = []

#     for i in range(n):
#         mat.append(list(map(int, sys.stdin.readline().split())))
        
#     cnt = 0
    
#     while True:
#         if clean(mat, r, c, cnt) == 1:
#             # 청소되지 않은 빈칸이 없는 경우
#             if check_not_cleaned(mat, n, m, r, c) == 0:
#                 # 뒤로 후진 가능하다면
#                 if check_back(mat, r, c, d) == 0:
#                     continue
                
#                 # 후진 할 수 없다면
#                 else:
#                     break
            
#             # 청소되지 않은 빈칸이 있는 경우
#             else:
#                 rotate(d)
#                 check_front(mat, r, c, d)
        
#         else:
#             if check_not_cleaned(mat, n, m, r, c) == 0:
#                 # 뒤로 후진 가능하다면
#                 if check_back(mat, r, c, d) == 0:
#                     continue
                
#                 # 후진 할 수 없다면
#                 else:
#                     break
                
#             # 청소되지 않은 빈칸이 있는 경우
#             else:
#                 rotate(d)
#                 check_front(mat, r, c, d)
                
#     print(cnt)
    
    
# if __name__ == "__main__":
#     main()
            
    
import sys

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 북, 동, 남, 서 방향 정의 (d가 0, 1, 2, 3일 때)
# dx: 행(row) 변화, dy: 열(col) 변화
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소한 칸의 수
cleaned_count = 0

while True:
    # 1. 현재 위치를 청소한다.
    if board[r][c] == 0:
        board[r][c] = 2  # 2는 청소 완료를 의미
        cleaned_count += 1

    # 2. 주변 4칸을 탐색한다.
    found_to_clean = False
    for _ in range(4):
        # 현재 방향에서 왼쪽으로 회전
        d = (d + 3) % 4
        
        # 회전한 방향의 앞쪽 칸 좌표 계산
        nx, ny = r + dx[d], c + dy[d]

        # 앞쪽 칸이 청소되지 않은 빈 공간이라면
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            # 그 방향으로 한 칸 전진
            r, c = nx, ny
            found_to_clean = True
            break # 탐색 중단하고 1번부터 다시 시작
            
    # 2-b. 주변 4칸 중 청소할 공간이 없다면
    if not found_to_clean:
        # 후진할 칸 좌표 계산 (현재 방향을 유지한 채 뒤로)
        back_r, back_c = r - dx[d], c - dy[d]

        # 후진할 수 있다면 후진
        if 0 <= back_r < n and 0 <= back_c < m and board[back_r][back_c] != 1:
            r, c = back_r, back_c
        # 후진할 수 없다면 (뒤가 벽이라면)
        else:
            break # 작동을 멈춘다

print(cleaned_count)