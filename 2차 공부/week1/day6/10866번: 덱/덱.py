import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for i in range(N):
    line = input().strip().split(' ')
    if len(line) == 2:
        command, num = line[0], int(line[1])
    else:
        command = line[0]
    if command == 'push_front':
        queue.insert(0, num)
    elif command == 'push_back':
        queue.append(num)
    elif command == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)