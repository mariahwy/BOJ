#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/10/17 12:00:16 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]

dp = [100001] * (k+1)

dp[0] = 0

for coin in coins:
    for j in range(coin, k+1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])

