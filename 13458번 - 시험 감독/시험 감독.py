#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13458                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13458                          #+#        #+#      #+#     #
#    Solved: 2025/10/16 15:12:51 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

n = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

student = [student[i] - b for i in range(len(student))]

res = n

for i in range(n):
    if student[i] > 0:
        if student[i] % c == 0:
            res += (student[i]//c)
        else: 
            res += (student[i]//c + 1)

print(res)