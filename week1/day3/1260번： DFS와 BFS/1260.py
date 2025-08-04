import sys
from collections import deque

def DFS(graph, start_node):
    visited = set()
    stack = [start_node]
    out_node_list = []

    while stack:
        out_node = stack.pop()

        if out_node not in visited:
            out_node_list.append(out_node)
            visited.add(out_node)

            for neighbor in reversed(graph[out_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return out_node_list

def BFS(graph, start_node):

    visited = set()
    queue = deque()
    queue.append(start_node)
    out_node_list = []

    while queue:
        out_node = queue.popleft()

        if out_node not in visited:
            out_node_list.append(out_node)
            visited.add(out_node)

            for neighbor in graph[out_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return out_node_list

# sys.stdin = open('./test.txt')
node_num, line_num, start_node = map(int, sys.stdin.readline().split())

graph = {}

for node_name in range(1, node_num+1):
    graph[node_name] = []

for row in sys.stdin:
    parent_node, child_node = map(int,row.split())
    graph[parent_node].append(child_node)
    graph[child_node].append(parent_node)

# 🔧 여기서 오름차순 정렬!
for key in graph:
    graph[key].sort()
    
dfs_result = DFS(graph, start_node)
bfs_result = BFS(graph, start_node)

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))

