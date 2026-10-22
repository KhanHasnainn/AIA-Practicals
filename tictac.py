b = [" "] * 9
wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]


p = "X"


while True:
    print(b[0:3], "\n", b[3:6], "\n", b[6:9])
    try:
        m = int(input(p + " position (1-9): ")) - 1
        if m not in range(9) or b[m] != " ":
            print("Invalid move")
            continue
    except ValueError:
        print("Enter a number")
        continue


    b[m] = p


    if any(all(b[i] == p for i in w) for w in wins):
        print(b)
        print(p, "wins!")
        break


    if " " not in b:
        print("Draw!")
        break


    p = "O" if p == "X" else "X"
