import sys
from collections import deque

# sys.stdin = open('./test.txt')
N = int(sys.stdin.readline().strip())
line_contents = [line.strip() for line in sys.stdin.readlines()]
only_unique_contents = list(set(line_contents))

sorted_contents = sorted(only_unique_contents, key = lambda x : (len(x), x))
for content in sorted_contents:
    print(content)