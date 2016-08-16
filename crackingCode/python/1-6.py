# Given  an  image  represented  by  an  NxN  matrix,  where  each  pixel  in
# the  image  is  4 bytes, write a method to rotate the image by 90 degrees. Can
# you do this in place?

mat = [
    # [2, 6],
    # [2, 6]
    [2, 6, 8, 2, 5],
    [2, 6, 8, 2, 5],
    [2, 6, 8, 2, 5],
    [2, 6, 8, 2, 5],
    [2, 6, 8, 2, 5]
]

def rotate90(mat):
    n = len(mat)
    mat90 = [[] for x in range(n)]
    for x in range(n):
        mat90[x] = [row[x] for row in mat]
    return mat90

print rotate90(mat) if len(mat) == len(mat[0]) else "This ain't NxN, yo!"

def rot90(mat):
    mat90 = []
    for i in range(len(mat)):
        ary = []
        for j in range(len(mat[i])):
            ary.append(mat[j][i]) 
        mat90.append(ary)
    return mat90
