
graph = {
    '1': ['2', '3', '4'], '2': ['5', '6'],
    '3': [], '4': ['7', '8'], '5': ['9', '10'],
    '6': [], '7': ['11', '12'], '8': [],
    '9': [], '10': [], '11': [], '12': []
}

def dfs(node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        for n in graph[node]:
            dfs(n)

visited = []
print("DFS:")
dfs('1')
