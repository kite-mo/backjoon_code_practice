import sys

n = int(sys.stdin.readline())
num_range = list(range(1, n + 1))

stack = []
correct_arrays = [int(row) for row in sys.stdin.read().splitlines()]
count_num = 0

stack = []
result = []
for num in num_range:
    stack.append(num)
    result.append('+')

    while stack and stack[-1] == correct_arrays[count_num]:
        result.append('-')
        stack.pop()
        count_num+=1    

if count_num != len(correct_arrays):
    print('NO')
else:
    for re in result:
        print(re)