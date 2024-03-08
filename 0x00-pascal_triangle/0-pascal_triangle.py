#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
