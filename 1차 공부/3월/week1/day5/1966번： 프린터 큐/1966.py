import sys
from collections import deque

# sys.stdin = open('./test.txt')
problem_numbers = int(sys.stdin.readline().strip())
total_lines = sys.stdin.readlines()

for i in range(problem_numbers):
    problem = total_lines[i*2:i*2+2]
    document_numbers, place_index = list(map(int, problem[0].strip().split()))
    importance_list = deque(map(int, problem[1].strip().split()))
    importance_list = deque([(idx, num) for idx, num in enumerate(importance_list)])
    count = 0

    if document_numbers == 1:
        print(1)
    else:
        while importance_list:
            max_importance = max(importance_list, key=lambda x: x[1])[1]
            index, out_node = importance_list.popleft()
            if out_node < max_importance:
                importance_list.append((index, out_node))
            else:
                count +=1
                if index == place_index:
                    print(count)
