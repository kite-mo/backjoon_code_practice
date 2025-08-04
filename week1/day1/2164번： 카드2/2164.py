import sys
from collections import deque

read_contents = sys.stdin.readlines()
range_num = int(read_contents[0])

queue = deque()
for num in range(1, range_num +1):
    queue.append(num)

while len(queue) != 1:
    first_out_num = queue.popleft()
    second_out_num = queue.popleft()
    queue.append(second_out_num)

result = queue[0]
print(result)