import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maze = []

for _ in range(N):
    maze.append(list(map(int, input().strip())))

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

counts_dict = {}

for i in range(N):
    for j in range(N):

        if maze[i][j] == 0:
            continue
        
        queue = deque()
        start_x, start_y = i, j
        queue.append([start_x, start_y])

        counts = 0
        while queue:
            pop_x, pop_y = queue.popleft()

            if maze[pop_x][pop_y] != 0:
                maze[pop_x][pop_y] = 0
                counts += 1

            for i in range(4):
                move_x, move_y = pop_x + x[i], pop_y + y[i]
                if 0 <= move_x < N and 0 <= move_y < N and maze[move_x][move_y] == 1:
                    queue.append([move_x, move_y])

        counts_dict[(start_x, start_y)] = counts

sorted_values = sorted(counts_dict.values())

print(len(sorted_values))
for val in sorted_values:
    print(val)