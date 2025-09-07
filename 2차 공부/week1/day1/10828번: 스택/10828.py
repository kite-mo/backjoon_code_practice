import sys

line_num = int(sys.stdin.readline())
stack = []

for i in range(line_num):
    next_line = sys.stdin.readline()
    split_lines = next_line.split(' ')

    if len(split_lines) == 1:
        command = split_lines[0].split('\n')[0]
    else:
        command, number = split_lines[0], int(split_lines[1])

    if command == 'push':
        stack.append(number)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop_number = stack.pop()
            print(pop_number)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])