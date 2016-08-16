# Write an algorithm such that if an element in an MxN matrix is 0, its entire
# row and column is set to 0.

mat = [
    [2, 0, 1],
    [2, 6, 2]
    # [2, 6, 8, 2, 5],
    # [2, 6, 8, 0, 5],
    # [2, 6, 8, 2, 5],
    # [2, 6, 8, 2, 5],
    # [2, 6, 8, 2, 5]
]

def convert_zero(mat):
    convMat = mat[:] # list(mat)
    cols = []
    rows = []
    for rowIdx in range(len(convMat)):
        row = convMat[rowIdx]
        zeroes = []
        try:
            while row.index(0):
                idx = row.index(0)
                zeroes.append(idx)
                row[idx] = 1
        except:
            if len(zeroes) > 0:
                rows.append(rowIdx)
                cols = cols + zeroes
        print cols
        print rows
        if len(cols) > 0:
            for x in range(len(convMat)):
                for y in cols:
                    convMat[x][y] = 0
            for z in rows:
                convMat[z] = [0 for num in convMat[z]]
    return convMat

    # for rowIdx in range(len(convMat)):
    #     zCol = []
    #     row = convMat[rowIdx]
    #     for x in range(len(row)):
    #         if row[x] == 0:
    #             zCol.append(x)
    #     if len(zCol) > 0:

    # Check duplicates in zCol

print convert_zero(mat)









# obj = {
#     '1':[1, 1, 1, 0],
#     '2':[1, 1, 1, 1],
#     '3':[1, 1, 1, 1],
#     '4':[1, 0, 1, 1]
# }
#
# for key in obj.keys():
#     val = obj[key]
#     try:
#         val.index(0)
#         for item in val:
#             if item != 0:
#                 index = val.index(item)
#                 obj[key][index] = 0
#         print 'Row ' + key + " set to 0's"
#     except:
#         print 'Row ' + key + ' looks good!'
#
# print obj
