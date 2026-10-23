
def hill_climb():
    values = [1, 3, 6, 8, 7, 5, 2]
    i = 0

    while i < len(values)-1 and values[i+1] > values[i]:
        i += 1

    print("Best value:", values[i])

hill_climb()

