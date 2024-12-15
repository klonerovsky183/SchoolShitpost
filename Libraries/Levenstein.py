def edit_distance(firstString, secondString):
    firstLen = len(firstString)
    secondLen = len(secondString)
    
    matrix = [[0] * (secondLen + 1) for _ in range(firstLen + 1)]

    for x in range(firstLen + 1):
        matrix[x][0] = x
    for y in range(secondLen + 1):
        matrix[0][y] = y

    for x in range(1, firstLen + 1):
        for y in range(1, secondLen + 1):
            if firstString[x - 1] == secondString[y - 1]:
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                matrix[x][y] = min(matrix[x - 1][y] + 1,
                               matrix[x][y - 1] + 1,
                               matrix[x - 1][y - 1] + 1)
    
    for row in matrix:
        print(row)

    return matrix


def edit_sequence(firstString, secondString):
    firstLen = len(firstString)
    secondLen = len(secondString)
    matrix = edit_distance(firstString, secondString)

    operations = []
    x, y = firstLen, secondLen

    while x > 0 and y > 0:
        if firstString[x - 1] == secondString[y - 1]:
            operations.append((x - 1, y - 1))
            x -= 1
            y -= 1
        else:
            if matrix[x][y] == matrix[x - 1][y] + 1:
                operations.append((x - 1, -1))
                x -= 1
            elif matrix[x][y] == matrix[x][y - 1] + 1:
                operations.append((-1, y - 1))
                y -= 1
            else:
                operations.append((x - 1, y - 1))
                x -= 1
                y -= 1

    while x > 0:
        operations.append((x - 1, -1))
        x -= 1

    while y > 0:
        operations.append((-1, y - 1))
        y -= 1

    operations.reverse()

    if operations is None:
        try:
            operations.append((-1, y))
        except:
            operations.append((1, y - 1))

    return operations
