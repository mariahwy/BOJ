#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14501                          #+#        #+#      #+#     #
#    Solved: 2025/10/27 13:46:42 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# dfs + dp 메모이제이션
import sys
n = int(sys.stdin.readline())

schedule = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split(" "))
    schedule.append((t, p))

dp = [-1] * (n+1)

def dfs(day):
    if day >= n:
        return 0
    
    # 이미 계산한 날은 skip
    if dp[day] != -1:
        return dp[day]
    
    t, p = schedule[day]
    
    # 상담을 안 하기
    price_not_selected = dfs(day+1)
    
    # 상담 하기
    price_selected = 0
    end_date = day + t
    
    if end_date <= n:
        price_selected = p + dfs(end_date)
        
    dp[day] = max(price_not_selected, price_selected)
    return dp[day]

print(dfs(0))