import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split()))

N_deque = deque(range(1, N + 1)) # index unique 값으로 구성된 deque 라고 생각해보자
N_deque = deque([(idx+1, num) for idx, num in enumerate(N_deque)])

target_deque = deque(map(int, sys.stdin.readline().strip().split()))
func_count = 0

while target_deque:
    target_place = target_deque[0]
    half_size = len(N_deque) // 2
    
    for target_index, (N_index, N_num) in enumerate(N_deque):
        if N_index == target_place:
            break
        
    if target_index == 0:
        N_deque.popleft()
        target_deque.popleft()
    
    elif target_index <= half_size:
        for i in range(target_index):
            N_deque.append(N_deque.popleft())
            func_count += 1
        N_deque.popleft()
        target_deque.popleft()
    
    else:
        for i in range(len(N_deque) - target_index):
            N_deque.appendleft(N_deque.pop())
            func_count += 1
        N_deque.popleft()
        target_deque.popleft()

print(func_count)