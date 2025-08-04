import sys

def check_clean_room(room_array, start_x, start_y, N, M):
    move_range = [(1,0), (-1,0), (0,1), (0,-1)]
    check_num = set([])
    room_available = False

    for move_x, move_y in move_range:
        dx, dy = start_x+move_x, start_y+move_y 

        if 0 <= dx < N and 0 <= dy < M:
            room_status = room_array[dx][dy]
            check_num.add(room_status)

    if 0 not in check_num:
        return room_available
    else:
        room_available = True
        return room_available
    
def check_return_case(room_array, start_x, start_y, robot_direction, N, M, robot_running):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    return_direction = (robot_direction+2)%4
    dx, dy = start_x + dx[return_direction], start_y + dy[return_direction]

    if 0<=dx<N and 0<=dy<M and room_array[dx][dy] == 1:
        robot_running = False
        return dx, dy, robot_running
    else:
        return dx, dy, robot_running

def clean_room_status(room_array, start_x, start_y, robot_direction, N, M):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    reverse_clock_direction = robot_direction

    for i in range(4):
        reverse_clock_direction = (reverse_clock_direction + 3) % 4
        move_x, move_y = start_x + dx[reverse_clock_direction], start_y + dy[reverse_clock_direction]

        if 0<=move_x<N and 0<=move_y<M and room_array[move_x][move_y] == 0:
            return move_x, move_y, reverse_clock_direction

# sys.stdin = open('./test.txt')

N, M = list(map(int, sys.stdin.readline().strip().split()))
start_x, start_y, robot_direction = list(map(int, sys.stdin.readline().strip().split()))
room_array = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]

# 시작 위치 청소
room_array[start_x][start_y] = 2
count_clean = 0
count_clean += 1
robot_running = True
while robot_running:
    room_available = check_clean_room(room_array, start_x, start_y, N, M)
    if not room_available:
        start_x, start_y, robot_running = check_return_case(
            room_array, start_x, start_y, robot_direction, N, M, robot_running
        )
    else:
        start_x, start_y, robot_direction = clean_room_status(
            room_array, start_x, start_y, robot_direction, N, M
        )
        room_array[start_x][start_y] = 2
        count_clean += 1

print(count_clean)