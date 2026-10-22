
def hanoi(n, A, B, C, a="A", b="B", c="C"):
    if n == 1:
        C.append(A.pop())
        print("Move disk from", a, "to", c)
        print("A:", A, "\nB:", B, "\nC:", C)
        return

    hanoi(n-1, A, C, B, a, c, b)
    hanoi(1, A, B, C, a, b, c)
    hanoi(n-1, B, A, C, b, a, c)

n = int(input("Enter disks: "))
A = list(range(n, 0, -1))
B = []
C = []

print("Initial state")
print("A:", A, "\nB:", B, "\nC:", C)

hanoi(n, A, B, C)
