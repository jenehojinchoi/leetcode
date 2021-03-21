# <Problem Statement>
# There is a maze with a size of N * M
print('What is your input of n, m? Type n m: ')
n, m - map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x,y):
    queue = deque()
    queue.append(x,y)
    while queue:
        x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny <0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue 
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))