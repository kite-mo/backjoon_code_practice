import sys

# sys.stdin = open('./test.txt')
N, K = map(int, sys.stdin.readline().strip().split())

first_circle = list(range(1, N+1))

out_pop_list = []
while first_circle:
    first_circle = first_circle[K-1:] + first_circle[:K-1]
    out_pop = first_circle.pop(0)
    out_pop_list.append(out_pop)

result = "<" + ", ".join(map(str, out_pop_list)) + ">"
print(result)