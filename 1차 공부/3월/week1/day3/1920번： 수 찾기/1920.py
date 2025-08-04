import sys

# sys.stdin = open('./test.txt')

# 이진 탐색 시에는 반드시 후보는 정렬을 해야함
N, N_list = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
M, M_list = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))

def binary_search(search_list, target):
    left, right = 0, len(search_list) - 1
    while left <= right:
        mid = (left + right)//2
        if search_list[mid] == target:
            return 1
        elif search_list[mid] < target:
            left = mid + 1
        elif search_list[mid] > target:
            right = mid - 1
    return 0

for target in M_list:
   result = binary_search(N_list, target)
   print(result) 