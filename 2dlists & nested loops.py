number_grid = [
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [0]
]

print(number_grid[0][2])

for row in number_grid:
    print(row)

print("\n")

for row in number_grid:
    for col in row:
        print(col)