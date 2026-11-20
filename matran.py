matrix = []
count = 1
for i in range(3):  # 3 dòng
    row = []
    for j in range(3):  # 3 cột
        row.append(count)
        count += 1
    matrix.append(row)

print(matrix)
