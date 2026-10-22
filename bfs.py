

graph = {
    '1': ['2', '3', '4'], '2': ['5', '6'],
    '3': [], '4': ['7', '8'], '5': ['9', '10'],
    '6': [], '7': ['11', '12'], '8': [],
    '9': [], '10': [], '11': [], '12': []
}


def bfs(node):
    visited = [node]
    q = [node]


    while q:
        n = q.pop(0)
        print(n, end=" ")
        for x in graph[n]:
            if x not in visited:
                visited.append(x)
                q.append(x)


print("BFS:")
