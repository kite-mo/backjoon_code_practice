# import sys
# import heapq

# sys.stdin = open('./test.txt')
# N, M, K = map(int, sys.stdin.readline().split())

# N_array = [[5]*(N) for i in range(N)]

# A_array = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# tree_array = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
# tree_info_array = [(array[2], [array[0]-1, array[1]-1, True]) for array in tree_array]

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, -1, -1, -1, 0, 1, 1, 1]

# for k in range(K):

#     sorted_tree_array = []
#     heapq.heappush(sorted_tree_array, tree_info_array)
#     sorted_tree_array = sorted_tree_array[0]

#     # spring
#     spring_tree_array = []
#     for i in range(len(sorted_tree_array)):
#         tree_info = heapq.heappop(sorted_tree_array)
#         age, other_info = tree_info
#         x, y, alive = other_info

#         if N_array[x][y] >= age:
#             N_array[x][y] -= age
#             age += 1
#         else:
#             alive = False

#         new_info = [x, y, age, alive]
#         spring_tree_array.append(new_info)
    
#     # summer
#     summer_tree_array = []
#     for tree_info in spring_tree_array:
#         x, y, age, alive = tree_info
#         if alive == False:
#             N_array[x][y] += age//2
#         else:
#             summer_tree_array.append(tree_info)
            
#     # fall
#     fall_tree_array = []
#     for tree_info in summer_tree_array:
#         x, y, age, alive = tree_info
#         fall_tree_array.append((age, [x, y, alive]))
#         if age % 5 == 0:
#             for i in range(8):
#                 new_x, new_y = x + dx[i], y + dy[i]
#                 if 0<=new_x<N and 0<=new_y<N:
#                     age = 1
#                     alive = True
#                     fall_tree_array.append((age, [new_x, new_y, True]))

#     tree_info_array = fall_tree_array

#     # winter
#     for x in range(N):
#         for y in range(N):
#             N_array[x][y] += A_array[x][y]

# alive_tree_counts = sum([tree_info[1][-1] for tree_info in tree_info_array])
# print(alive_tree_counts)


# import sys
# import heapq

# # sys.stdin = open('./test.txt')
# N, M, K = map(int, sys.stdin.readline().split())

# N_array = [[5]*(N) for i in range(N)]

# A_array = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
# tree_array = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
# tree_info_array = [(array[2], [array[0]-1, array[1]-1, True]) for array in tree_array]

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, -1, -1, -1, 0, 1, 1, 1]

# for k in range(K):

#     sorted_tree_array = []
#     heapq.heappush(sorted_tree_array, tree_info_array)
#     sorted_tree_array = sorted_tree_array[0]

#     # spring
#     spring_tree_array = []
#     for i in range(len(sorted_tree_array)):
#         tree_info = heapq.heappop(sorted_tree_array)
#         age, other_info = tree_info
#         x, y, alive = other_info

#         if N_array[x][y] >= age:
#             N_array[x][y] -= age
#             age += 1
#         else:
#             alive = False

#         new_info = [x, y, age, alive]
#         spring_tree_array.append(new_info)
    
#     # summer
#     summer_tree_array = []
#     for tree_info in spring_tree_array:
#         x, y, age, alive = tree_info
#         if alive == False:
#             N_array[x][y] += age//2
#         else:
#             summer_tree_array.append(tree_info)
            
#     # fall
#     fall_tree_array = []
#     for tree_info in summer_tree_array:
#         x, y, age, alive = tree_info
#         fall_tree_array.append((age, [x, y, alive]))
#         if age % 5 == 0:
#             for i in range(8):
#                 new_x, new_y = x + dx[i], y + dy[i]
#                 if 0<=new_x<N and 0<=new_y<N:
#                     age = 1
#                     alive = True
#                     fall_tree_array.append((age, [new_x, new_y, True]))

#     tree_info_array = fall_tree_array

#     # winter
#     for x in range(N):
#         for y in range(N):
#             N_array[x][y] += A_array[x][y]

# alive_tree_counts = sum([tree_info[1][-1] for tree_info in tree_info_array])
# print(alive_tree_counts)

import sys
from collections import deque

# sys.stdin = open('./test.txt')
N, M, K = map(int, sys.stdin.readline().split())

N_array = [[5]*(N) for i in range(N)]
A_array = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
tree_array = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
tree_deque_array = [[deque() for i in range(N)] for i in range(N)]
for tree_info in tree_array:
    x, y, age = tree_info
    tree_deque_array[x-1][y-1].appendleft(age)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for k in range(K):

    fall_tree_index = []
    # spring and summer
    for x in range(N):
        for y in range(N):
            new_queue = deque()
            energy = 0
            while tree_deque_array[x][y]:
                age = tree_deque_array[x][y].popleft()
                if N_array[x][y] >= age:
                    N_array[x][y] -= age
                    age += 1
                    new_queue.append(age)
                    if age % 5 == 0:
                        fall_tree_index.append([x, y])
                else:
                    energy += age//2

            N_array[x][y] += energy
            tree_deque_array[x][y] = new_queue

    # fall
    if len(fall_tree_index) > 0:
        for x, y in fall_tree_index:
            for i in range(8):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0<=new_x<N and 0<=new_y<N:
                    tree_deque_array[new_x][new_y].appendleft(1)

    # winter
    for x in range(N):
        for y in range(N):
            N_array[x][y] += A_array[x][y]

count = 0
for i in range(N):
    for j in range(N):
        if len(tree_deque_array[i][j]) > 0:
            count += len(tree_deque_array[i][j])

print(count)