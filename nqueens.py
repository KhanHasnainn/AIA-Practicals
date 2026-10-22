def safe(b, r, c):
    for i in range(r):
        if b[i] == c or abs(b[i]-c) == r-i:
            return False
    return True


def solve(b, r, n):
    if r == n:
        for i in range(n):
            print(" ".join("Q" if b[i] == j else "."
                           for j in range(n)))
        print()
        return


    for c in range(n):
        if safe(b, r, c):
            b[r] = c
            solve(b, r+1, n)
            b[r] = -1


n = int(input("Enter N: "))
solve([-1]*n, 0, n)
