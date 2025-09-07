import sys

# sys.stdin = open('./test.txt')
contents = sys.stdin.read().split()
contents_num = list(map(int, contents))
first_num, question_num = contents_num[0], contents_num[1:]
for i in sorted(question_num):
    print(i)