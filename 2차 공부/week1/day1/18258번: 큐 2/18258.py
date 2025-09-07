import sys
from collections import deque

line_num = int(sys.stdin.readline())
queue = deque()

for i in range(line_num):
    next_line = sys.stdin.readline().rstrip()
    split_line = next_line.split(' ')

    if len(split_line) == 1:
        command = split_line[0]
    else:
        command, number = split_line[0], int(split_line[1])

    if command == 'push':
        queue.append(number)
    elif command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            pop_number = queue.popleft()
            print(pop_number)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])