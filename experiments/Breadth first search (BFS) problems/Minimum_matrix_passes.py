from collections import deque

# Given a MxN matrix of integers whose each cell can contain a negative, zero or
# positive value, determine the minimum number of passes required to convert all
# negative values in the matrix to positive

# Use to get adjacent position
row = [-1, 0, 0, 1]
column = [0, -1, 1, 0]

Q = deque()
q = deque()

def find_coordinates(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > 0:
                Q.append((i, j))




if __name__ == '__main__':
    mat = [
        [-1, -9,  0, -1,  0],
        [-8, -3, -2,  9, -7],
        [2,   0,  0, -6,  0],
        [0,  -7, -3,  5, -4]
    ]

    find_coordinates(mat)
    print(Q)
