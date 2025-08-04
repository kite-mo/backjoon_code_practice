import sys
from collections import deque

# sys.stdin = open('./test.txt')

tok_list = [deque([int(j) for j in sys.stdin.readline().strip().split()[0]]) for i in range(4)]
make_key = [12, 1.5, 3, 4.5, 6, 7.5, 9, 10.5]
tok_dict = {}
for tok_num in range(0, len(tok_list)):
    tok_dict[tok_num+1] = {key : tok_list[tok_num][num] for num, key in enumerate(make_key)}

rotate_nums = int(sys.stdin.readline().strip())
rotate_info_list = []
for i in range(rotate_nums):
    info = list(map(int, sys.stdin.readline().strip().split()))
    rotate_info_list.append(info)

def change_took_by_direction(queue, direction):
    if direction == 1:
        queue.appendleft(queue.pop())
    if direction == -1:
        queue.append(queue.popleft())
    new_direction = direction * -1
    return queue, new_direction

first_tok, second_tok, thrid_tok, fourth_tok = tok_list

count = 0

for rotate_num in range(rotate_nums):

    first_tok, second_tok, thrid_tok, fourth_tok = tok_list

    tok_num, direction = rotate_info_list[rotate_num]
    tok_num = tok_num - 1

    tok_part_same_12 = first_tok[2] != second_tok[-2]
    tok_part_same_23 = second_tok[2] != thrid_tok[-2]
    tok_part_same_34 = thrid_tok[2] != fourth_tok[-2]

    if tok_num == 0:
        new_tok, new_direction = change_took_by_direction(tok_list[tok_num], direction)
        tok_list[tok_num] = new_tok

        if tok_part_same_12:
            new_tok, new_direction = change_took_by_direction(tok_list[tok_num+1], new_direction)
            tok_list[tok_num+1] = new_tok

            if tok_part_same_23:
                new_tok, new_direction = change_took_by_direction(tok_list[tok_num+2], new_direction)
                tok_list[tok_num+2] = new_tok

                if tok_part_same_34:
                    new_tok, new_direction = change_took_by_direction(tok_list[tok_num+3], new_direction)
                    tok_list[tok_num+3] = new_tok
    
    if tok_num == 3:
        new_tok, new_direction = change_took_by_direction(tok_list[tok_num], direction)
        tok_list[tok_num] = new_tok

        if tok_part_same_34:
            new_tok, new_direction = change_took_by_direction(tok_list[tok_num-1], new_direction)
            tok_list[tok_num-1] = new_tok

            if tok_part_same_23:
                new_tok, new_direction = change_took_by_direction(tok_list[tok_num-2], new_direction)
                tok_list[tok_num-2] = new_tok

                if tok_part_same_12:
                    new_tok, new_direction = change_took_by_direction(tok_list[tok_num-3], new_direction)
                    tok_list[tok_num-3] = new_tok
    

    if tok_num == 1:
        new_tok, new_direction = change_took_by_direction(tok_list[tok_num], direction)
        tok_list[tok_num] = new_tok

        if tok_part_same_12:
            new_tok, new_direction_ = change_took_by_direction(tok_list[tok_num-1], new_direction)
            tok_list[tok_num-1] = new_tok
        
        if tok_part_same_23:
            new_tok, new_direction = change_took_by_direction(tok_list[tok_num+1], new_direction)
            tok_list[tok_num+1] = new_tok

            if tok_part_same_34:
                new_tok, new_direction = change_took_by_direction(tok_list[tok_num+2], new_direction)
                tok_list[tok_num+2] = new_tok

    
    if tok_num == 2:
        new_tok, new_direction = change_took_by_direction(tok_list[tok_num], direction)
        tok_list[tok_num] = new_tok

        if tok_part_same_34:
            new_tok, new_direction_ = change_took_by_direction(tok_list[tok_num+1], new_direction)
            tok_list[tok_num+1] = new_tok
        
        if tok_part_same_23:
            new_tok, new_direction = change_took_by_direction(tok_list[tok_num-1], new_direction)
            tok_list[tok_num-1] = new_tok

            if tok_part_same_12:
                new_tok, new_direction = change_took_by_direction(tok_list[tok_num-2], new_direction)
                tok_list[tok_num-2] = new_tok

rotate_count = sum([tok[0]*2**(num) for num, tok in enumerate(tok_list)])
count += rotate_count

print(count)