#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9095                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9095                           #+#        #+#      #+#     #
#    Solved: 2025/10/17 12:41:03 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

t = int(sys.stdin.readline())

cases = [int(sys.stdin.readline()) for _ in range(t)]
    
dp = [0] * 11

# 초기값
dp[0] = 1
dp[1] = 1
dp[2] = 2

for case in cases:
    for i in range(3, case + 1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
    print(dp[case])