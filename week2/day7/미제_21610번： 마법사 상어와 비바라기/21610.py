import sys

# sys.stdin = open('./test.txt')
N, M = map(int, sys.stdin.readline().split())
N_array = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
d_s_list = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud_position = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]

for d, s in d_s_list:
    move_cloud_position = []
    for position in cloud_position:
        x, y = position
        new_x, new_y = (x + dx[d-1]*s)%N,(y + dy[d-1]*s)%N
        move_cloud_position.append((new_x, new_y))
        N_array[new_x][new_y] +=1
    
    for x, y in move_cloud_position:
        count = 0
        for d in [1, 3, 5, 7]:
            x_, y_ = x + dx[d], y + dy[d]
            if 0<=x_<N and 0<=y_<N and N_array[x_][y_] > 0:
                count+=1
        N_array[x][y] += count

    make_new_cloud_position = []
    before_cloud_position = set(move_cloud_position)
    for r in range(N):
        for c in range(N):
            if N_array[r][c] >= 2 and (r,c) not in before_cloud_position:
                make_new_cloud_position.append((r,c))
                N_array[r][c] -= 2
    
    cloud_position = make_new_cloud_position

total_sum = sum(map(sum, N_array))
print(total_sum)