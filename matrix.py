# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a = [[el for el in range(1, 4)] for i in range(3)]
# print(a)
# print(c[2][:2])
# print(c[1][2])
#
# for i in range(len(c)):
#     for j in range(len(c)):
# if i == j:
#     print(c[i][j])
# if i + j == len(c) - 1:
#     print(c[i][j])
# if i < j:
#     print(c[i][j])
#         if i + j < len(c) - 1:
#             print(c[i][j])

# TODO:
# 1: Посчитать сумму каждой строки  матрицы:
# 2: Посчитать сумму каждого столбца матрицы:
# 3: Поменять местами чётные и нечётные строки в матрице(Если в матрице
# нечётное количество строк, то последняя строка остаётся на месте:

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,13,15,16]]

#
# def sum_(matrix):
#     summed_list = [sum(i) for i in matrix]
#     print(summed_list)
#
#
# sum_(matrix)

sum_col = []

for j in range(len(matrix)):
    s = 0
    for i in range(len(matrix)):
        s += matrix[i][j]
    sum_col.append(s)
print(sum_col)

for i in range(0, len(matrix), 2):
    print(*matrix[i + 1])
    print(*matrix[i])
