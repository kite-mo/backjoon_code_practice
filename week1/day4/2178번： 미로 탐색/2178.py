import sys
from collections import deque

# sys.stdin = open('./test.txt')
N, M = list(map(int, sys.stdin.readline().split(' ')))

maze = []
for line in sys.stdin:
    maze.append([int(line[idx]) for idx in range(M)])

def maze_bfs(maze, start_x, start_y, N, M):
    queue = deque()
    queue.append((start_x, start_y))
    move_range = [(1,0), (-1,0), (0,-1), (0,1)]
    maze[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for move_x, move_y in move_range:
            nx = x + move_x
            ny = y + move_y

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze

# 실행
maze_ = maze_bfs(maze, start_x=0, start_y=0, N=N, M=M)
print(maze_[N-1][M-1])
