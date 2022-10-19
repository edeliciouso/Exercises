m = int(input("insert number: "))
n = int(input("insert number: "))

def game_with_cells(m, n):
    x = 1
    y = 1
    for i in range(1, m + 1, 2):
        if i > 2:
            x += 1
    for i in range(1, n + 1, 2):
        if i > 2:
            y += 1
    return x * y

print(game_with_cells(m, n))
