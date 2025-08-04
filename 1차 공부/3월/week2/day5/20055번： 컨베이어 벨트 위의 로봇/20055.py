import sys
from collections import deque

# sys.stdin = open('./test.txt')
N, K = list(map(int, sys.stdin.readline().strip().split()))

durability_list = list(map(int, sys.stdin.readline().strip().split()))
durability_dict = {
    i : d for i, d in enumerate(durability_list)
}
belt_queue = deque([(i, n) for i, n in enumerate(range(1, 2*N+1))])
robot_queue = deque([[i, 0] for i, n in enumerate(range(1, 2*N+1))])

# start
count = 0
robot_setup_index = 0
robot_drop_index = N-1

# initial robot setup
robot_queue[robot_setup_index][1] = 1
durability_dict[robot_setup_index] = durability_dict[robot_setup_index] - 1

belt_keep_moving = True
while belt_keep_moving:
    count += 1

    # first : move with belt
    belt_queue.appendleft(belt_queue.pop())
    robot_queue.appendleft(robot_queue.pop())

    ## remove N box 
    robot_queue[robot_drop_index][1] = 0

    # second : move robot with condition
    ## 가장 먼저 올라간 로봇 순서
    for robot_index in range(2*N-1, -1,-1):
        robot_exist = robot_queue[robot_index][1] == 1
        if robot_exist:
            next_robot_not_exist = robot_queue[robot_index-2*N+1][1] == 0
            durability_exist = durability_dict[belt_queue[robot_index-2*N+1][0]] != 0

            if (next_robot_not_exist and durability_exist):
                robot_queue[robot_index][1] = 0
                robot_queue[robot_index-2*N+1][1] = 1
                durability_dict[belt_queue[robot_index-2*N+1][0]] = durability_dict[belt_queue[robot_index-2*N-1][0]] - 1

                ## remove N box 
                robot_queue[robot_drop_index][1] = 0
    
    # thrid : setup new robot
    if durability_dict[belt_queue[0][0]] != 0:
        robot_queue[0][1] = 1
        durability_dict[belt_queue[0][0]] = durability_dict[belt_queue[0][0]] - 1
    
    count_k = 0
    for key, val in durability_dict.items():
        if val == 0:
            count_k += 1
    
    if count_k == K:
        belt_keep_moving = False

print(count)