import numpy as np

N = int(input())
matrix = [list(map(int, input().split())) for line in range(N)]
new_matrix = []
for i in range(N):
    new_matrix.append(matrix[i][::-1])
d = {i: [sum(np.diagonal(new_matrix, offset = i)), len(np.diagonal(new_matrix, offset = i))] for i in range(-N + 1, N)}
new_d = sorted(d.items(), key = lambda pair: (pair[1][0], -pair[1][1]))
print(*np.diagonal(new_matrix, offset = new_d[0][0]))
