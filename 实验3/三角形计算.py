'''
@Author 浊玉
@Description  
@Date create in 2023/5/12 13：20
'''


import math

vertices = {}

# 从键盘输入三个顶点坐标
for i in range(1, 4):
    x, y = input(f"请输入第{i}个顶点坐标，格式为x,y：").split(',')
    vertices[i] = (float(x), float(y))

# 计算三角形边长
a = math.sqrt((vertices[1][0]-vertices[2][0])**2 + (vertices[1][1]-vertices[2][1])**2)
b = math.sqrt((vertices[1][0]-vertices[3][0])**2 + (vertices[1][1]-vertices[3][1])**2)
c = math.sqrt((vertices[2][0]-vertices[3][0])**2 + (vertices[2][1]-vertices[3][1])**2)

# 计算半周长
s = (a + b + c) / 2

# 计算面积 这里用的是海龙公式
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# 输出结果
print(f"三角形面积为：{area}")
