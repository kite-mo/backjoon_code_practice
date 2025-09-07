import sys

# sys.stdin = open('./test.txt')
contents = [int(i) for i in sys.stdin.readlines()]
range_num = contents[0]
question_num = contents[1:]

for i in sorted(question_num):
    print(i)