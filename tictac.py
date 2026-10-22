from collections import deque


def water_jug(a, b, target):
    q = deque([((0, 0), [(0, 0)])])
    visited = set()


    while q:
        (x, y), path = q.popleft()


        if (x, y) in visited:
            continue
        visited.add((x, y))


        if x == target or y == target:
            print("Solution Steps:")
            for s in path:
                print(s)
            return


        states = [
            (a, y), (x, b), (0, y), (x, 0),
            (max(0, x-(b-y)), min(b, x+y)),
            (min(a, x+y), max(0, y-(a-x)))
        ]


        for s in states:
            if s not in visited:
                q.append((s, path+[s]))


    print("No solution")


water_jug(4, 3, 2)
