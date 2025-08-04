import sys
from collections import deque

# sys.stdin = open('./test.txt')
command_counts = int(sys.stdin.readline())

queue_ = deque()
list_ = []

for i in range(command_counts):
    contents = sys.stdin.readline().strip().split()

    if len(contents) == 2:
        command, number = contents[0], int(contents[1])
    else:
        command = contents[0]
    
    if command == 'push_front':
        queue_.appendleft(number)
    if command == 'push_back':
        queue_.append(number)
    if command == 'pop_front':
        if len(queue_) == 0:
            print(-1)
        else:
            out_number = queue_.popleft()
            print(out_number)
    if command == 'pop_back':
        if len(queue_) == 0:
            print(-1)
        else:
            out_number = queue_.pop()
            print(out_number)
    if command == 'size':
        print(len(queue_))
    if command == 'empty':
        if len(queue_) == 0:
            print(1)
        else:
            print(0)
    if command == 'front':
        if len(queue_) == 0:
            print(-1)
        else:
            print(queue_[0])
    if command == 'back':
        if len(queue_) == 0:
            print(-1)
        else:
            print(queue_[-1])