'''
@Author 浊玉
@Description  
@Date create in 2023/5/12 13：00
'''


#矩阵不采用输入的方法，直接赋值为元组
matrix = ((1, 2, 3, 4, 5),
          (6, 7, 8, 9, 10),
          (11, 12, 13, 14, 15),
          (16, 17, 18, 19, 20),
          (21, 22, 23, 24, 25))

# 输出矩阵元素
for i in range(5):
    for j in range(5):
        print("%2d " % matrix[i][j], end="")
    print()

# 计算左上到右下的对角线元素之和
sum1 = sum(matrix[i][i] for i in range(5))

# 计算右上到左下的对角线元素之和
sum2 = sum(matrix[i][4-i] for i in range(5))

print("左上到右下的对角线元素之和为：%d" % sum1)
print("右上到左下的对角线元素之和为：%d" % sum2)
