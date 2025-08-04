import sys

# sys.stdin = open('./test.txt')

contents = sys.stdin.readlines()

range_num = int(contents[0])
pair_int = [list(map(int, str_pair.split())) for str_pair in contents[1:]]

x_list, y_list = [], []
for x, y in pair_int:
    x_list.append(x)
    y_list.append(y)

equal_count = 0
x_list.sort()
x