#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2565                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2565                           #+#        #+#      #+#     #
#    Solved: 2025/10/17 14:13:24 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline()) # <=100

line = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    line.append((a, b))
  
line.sort(key = lambda x: x[0])

dp = [1] * (n)

b_line = [line[i][1] for i in range(len(line))]

for i in range(1, n):
    for j in range(i):
        # 증가 조건 만족
        if b_line[i] > b_line[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(n - max(dp))
        


    
