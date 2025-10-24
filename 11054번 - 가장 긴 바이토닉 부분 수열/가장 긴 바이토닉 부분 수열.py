#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11054                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11054                          #+#        #+#      #+#     #
#    Solved: 2025/10/17 15:57:56 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

increase_dp = [1] * n
# 원래 증가 수열
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j]+1)
max1 = max(increase_dp)

# 반대 증가 수열
decrease_dp = [1] * n
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j]+1)
max2 = max(decrease_dp)

# 각 후보뱔 합 - 1
result = [0] * n
for i in range(n):
    result[i] = increase_dp[i] + decrease_dp[i] - 1
    
print(max(result))
