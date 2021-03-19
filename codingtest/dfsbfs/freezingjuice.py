# <Problem Statement>
# N * M size of an ice cube tray. 

print('What is your input of n? Type n:')
n = int(input())
print('What is your input of m? Type m: ')
m = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 | x >= n | y <= -1 | y >= m:
        return False
        
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)