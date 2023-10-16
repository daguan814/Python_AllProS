'''
@Author 浊玉
@Description  
@Date create in 2023/5/26 19:38
'''

ls = ['中国', '美国', '日本', '法国', '意大利']
# 将列表元素用"$"连接成一个字符串
data = '$'.join(ls)
# 将字符串写入文本文件  这里用到了with的文本管理
with open('data.txt', 'w') as file:
    file.write(data)

# 从文本文件中读取数据
with open('data.txt', 'r') as file:
    allData = file.read()

# 输出读取的内容
print(allData)
