maze = [
    [1,1,0,1],
    [0,1,1,1],
    [0,1,1,0],
    [1,1,1,1]
]


R, C = 4, 4
visited = set()
path = []


def dfs(x, y):
    if (x < 0 or y < 0 or x >= R or y >= C
        or maze[x][y] == 0 or (x,y) in visited):
        return False


    visited.add((x,y))
    path.append((x,y))


    if (x,y) == (R-1,C-1):
        return True


    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        if dfs(x+dx, y+dy):
            return True


    path.pop()
    return False


if dfs(0,0):
    print("Path Found:", path)
else:
    print("No Path Found")
