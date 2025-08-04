# import sys
# from collections import deque

# # sys.stdin = open('./test.txt')
# R, C, T = map(int, sys.stdin.readline().split())

# room_array = []
# clean_machine_index_list = []
# room_index_dict = {}

# for idx, line in enumerate(sys.stdin.readlines()):
#     room_row = list(map(int, line.strip().split()))
#     room_array.append(room_row)

#     if room_row[0] == -1:
#         clean_machine_index_list.append(idx)

# def spread(R, C, r, c, room_array, clean_machine_index_list):
#     dx = [-1, 0, +1, 0]
#     dy = [0, +1, 0, -1]

#     spread_value = int(room_array[r][c]/5)
#     spread_dict = {}
#     sum_spread_value = 0
#     for i in range(4):
#         new_r, new_c = r + dx[i], c + dy[i]
        
#         if new_c == 0 and new_r in clean_machine_index_list:
#             continue

#         if 0<=new_r<R and 0<=new_c<C:
#             spread_dict[(new_r, new_c)] = spread_value
#             sum_spread_value += spread_value
    
#     spread_dict[(r,c)] = room_array[r][c] - sum_spread_value

#     return spread_dict

# def blow_aircleaning(R, C, clean_machine_index_list, room_array):
#     top = clean_machine_index_list[0]
#     bottom = clean_machine_index_list[1]

#     # 반시계 
#     ## 위 -> 아래
#     for d in range(top-1, 0, -1):
#         room_array[d][0] = room_array[d-1][0]
#     ## 오 -> 왼
#     for l in range(C-1):
#         room_array[0][l] = room_array[0][l+1]
#     ## 아래 -> 위
#     for u in range(0, top):
#         room_array[u][C-1] = room_array[u+1][C-1]
#     ## 왼 -> 오
#     for r in range(C-1, 1, -1):
#         room_array[top][r] = room_array[top][r-1]
#     room_array[top][1] = 0
    
#     # 시계
#     ## 아래 -> 위
#     for u in range(bottom+1, R-1):
#         room_array[u][0] = room_array[u+1][0] 
#     ## 오 -> 왼
#     for l in range(C-1):
#         room_array[R-1][l] = room_array[R-1][l+1]
#     # 위 -> 아래
#     for d in range(R-1, bottom, -1):
#         room_array[d][C-1] = room_array[d-1][C-1]
#     ## 왼 -> 오
#     for r in range(C-1, 1, -1):
#         room_array[bottom][r] = room_array[bottom][r-1]
#     room_array[bottom][1] = 0

#     return room_array


# for t in range(T):
#     spread_dict_list = []
#     room_index_dict = {}
    
#     # spread dust part
#     for r in range(R):
#         for c in range(C):
#             room_index_dict[(r,c)] = [0]
#             value = room_array[r][c]
#             if value > 0:
#                 spread_dict = spread(R, C, r, c, room_array, clean_machine_index_list)
#                 spread_dict_list.append(spread_dict)

#     for spread_dict in spread_dict_list:
#         for key, val in spread_dict.items():
#             room_index_dict[key].append(val)

#     for (r, c), list_val in room_index_dict.items():
#         room_array[r][c] = sum(list_val)

#     # blow air cleaning machine
#     room_array = blow_aircleaning(R, C, clean_machine_index_list, room_array)
    
#     for clean_machine_index in clean_machine_index_list:
#         room_array[clean_machine_index][0] = -1

# total_sum = sum([sum(array) for array in room_array]) + 2

# print(total_sum)


def spread(R, C, room_array):
    dx = [-1, 0, +1, 0]
    dy = [0, +1, 0, -1]

    new_array = [[0] * C for r in range(R)]

    # spread dust part
    for r in range(R):
        for c in range(C):
            value = room_array[r][c]
            if value > 0:
                spread_value = int(room_array[r][c]//5)
                sum_spread_value = 0
                for i in range(4):
                    new_r, new_c = r + dx[i], c + dy[i]
                    if 0 <= new_r < R and 0 <= new_c < C and room_array[new_r][new_c] != -1:
                        new_array[new_r][new_c] += spread_value
                        sum_spread_value += spread_value
                new_array[r][c] += value - sum_spread_value
            elif value == -1:
                new_array[r][c] = -1
    return new_array

def blow_aircleaning(R, C, clean_machine_index_list, room_array):
    top = clean_machine_index_list[0]
    bottom = clean_machine_index_list[1]

    # 반시계 
    ## 위 -> 아래
    for d in range(top-1, 0, -1):
        room_array[d][0] = room_array[d-1][0]
    ## 오 -> 왼
    for l in range(C-1):
        room_array[0][l] = room_array[0][l+1]
    ## 아래 -> 위
    for u in range(0, top):
        room_array[u][C-1] = room_array[u+1][C-1]
    ## 왼 -> 오
    for r in range(C-1, 1, -1):
        room_array[top][r] = room_array[top][r-1]
    room_array[top][1] = 0
    
    # 시계
    ## 아래 -> 위
    for u in range(bottom+1, R-1):
        room_array[u][0] = room_array[u+1][0] 
    ## 오 -> 왼
    for l in range(C-1):
        room_array[R-1][l] = room_array[R-1][l+1]
    # 위 -> 아래
    for d in range(R-1, bottom, -1):
        room_array[d][C-1] = room_array[d-1][C-1]
    ## 왼 -> 오
    for r in range(C-1, 1, -1):
        room_array[bottom][r] = room_array[bottom][r-1]
    room_array[bottom][1] = 0

    return room_array

import sys
from collections import deque

# sys.stdin = open('./test.txt')
R, C, T = map(int, sys.stdin.readline().split())

room_array = []
clean_machine_index_list = []

for idx, line in enumerate(sys.stdin.readlines()):
    room_row = list(map(int, line.strip().split()))
    room_array.append(room_row)

    if room_row[0] == -1:
        clean_machine_index_list.append(idx)

for t in range(T):

    room_array = spread(R, C, room_array)
    # blow air cleaning machine
    room_array = blow_aircleaning(R, C, clean_machine_index_list, room_array)

total_sum = sum([sum(array) for array in room_array]) + 2

print(total_sum)