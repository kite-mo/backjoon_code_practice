import sys
from collections import deque

# sys.stdin = open('./test.txt')
N = sys.stdin.readline().strip().split()
contents = [line.strip() for line in sys.stdin.readlines()]

def find_int_and_sum(string):
    sum_val = sum(map(int, ' '.join(x for x in string if x.isdigit()).split()))
    return sum_val

sorted_contents = sorted(contents, key = lambda x : (len(x), find_int_and_sum(x), x))

for content in sorted_contents:
    print(content)