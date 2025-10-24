#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2563                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: mariahwy <boj.kr/u/mariahwy>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2563                           #+#        #+#      #+#     #
#    Solved: 2025/10/17 16:11:46 by mariahwy      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(arr) * 4) # N * 4

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]
    
def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(start, mid, index*2 + 1, left, right)

print(interval_sum(0, len(arr) - 1, 1, 0, 2))