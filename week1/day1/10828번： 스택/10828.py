import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    row = sys.stdin.readline().strip().split()
    
    if len(row) > 1:
        command, num = row[0], int(row[1])
        stack.append(num)
    else:
        command = row[0] # 정수 
        if command == 'pop':
            print(stack.pop() if stack else -1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            print(0 if stack else 1)
        elif command == 'top':
            print(stack[-1] if stack else -1)