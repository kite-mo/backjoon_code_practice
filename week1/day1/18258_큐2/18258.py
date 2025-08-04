import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()

for _ in range(n):
    row = sys.stdin.readline().strip().split()
    if len(row) > 1:
        command, num = row[0], int(row[1])
        stack.append(num)
    else:
        command = row[0]
        if command == 'pop':
            print(stack.popleft() if stack else -1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            print(0 if stack else 1)
        elif command == 'front':
            print(stack[0] if stack else -1)
        elif command == 'back':
            print(stack[-1] if stack else -1)