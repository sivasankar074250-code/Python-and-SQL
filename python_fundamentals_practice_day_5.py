# python_practice_day_5

# 1. Interleave 2 Lists

a = [10, 20, 30, 40]
b = [1, 2, 3, 4]
result = []
for i in range(len(a)):
    result.extend([a[i], b[i]])
print("Interleaved list:", result)

# 2. Inventory Records

products = [("Sensor", 4, 150.0), ("Cable", 12, 25.0), ("Board", 3, 800.0)]
total = 0
low_stock = []
for name, quantity, price in products:
    value = quantity * price
    total += value
    print(f"{name}: Value = {value:.2f}")
    if quantity < 5:
        low_stock.append(name)
print("Low-stock products:", low_stock)
print(f"Total inventory value: {total:.2f}")

# 3. Extract Valid Measurements

readings = [8, 10, 20, 35, 51, 40]
converted = [round(c * 9 / 5 + 32, 1) for c in readings if 10 <= c <= 50]
print("Converted readings:", converted)

# 4. Run-Length Encoding

values = [4, 4, 4, 2, 2, 7, 7, 4, 4, 9]
compressed = []
for value in values:
    if compressed and compressed[-1][0] == value:
        previous, count = compressed[-1]
        compressed[-1] = (previous, count + 1)
    else:
        compressed.append((value, 1))
print("Compressed list:", compressed)

# 5. Sliding Window 

sales = [10, 20, 30, 40, 50, 60]
k = 3
averages = [round(sum(sales[i:i + k]) / k, 2) for i in range(len(sales) - k + 1)]
print("Window averages:", [f"{x:.2f}" for x in averages])

# 6. Rotate a Matrix 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
rotated = [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]
for row in rotated:
    print(*row)

# 7. Zigzag Matrix Traversal

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = []
for i, row in enumerate(matrix):
    result.extend(row if i % 2 == 0 else row[::-1])
print("Zigzag list:", result)

# 8. Sparse Matrix 

matrix = [[0, 0, 5, 0], [0, 8, 0, 0], [3, 0, 0, 6]]
sparse = [(i, j, matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] != 0]
print(sparse)

# 9. Matrix Multiplication 

a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]
if len(a[0]) != len(b):
    print("Error: Incompatible matrix dimensions")
else:
    result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
    print("Product matrix:")
    for row in result:
        print(*row)

# 10. Maximum-Sum Path 

matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
rows, cols = len(matrix), len(matrix[0])
dp = [[0] * cols for _ in range(rows)]
parent = [[None] * cols for _ in range(rows)]
dp[0][0] = matrix[0][0]
for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            continue
        top = dp[i - 1][j] if i > 0 else -1
        left = dp[i][j - 1] if j > 0 else -1
        if top > left:
            dp[i][j] = top + matrix[i][j]
            parent[i][j] = (i - 1, j)
        else:
            dp[i][j] = left + matrix[i][j]
            parent[i][j] = (i, j - 1)
path = []
i, j = rows - 1, cols - 1
while True:
    path.append(matrix[i][j])
    if (i, j) == (0, 0):
        break
    i, j = parent[i][j]
path.reverse()
print("Maximum path sum:", dp[-1][-1])
print("Path:", path)

