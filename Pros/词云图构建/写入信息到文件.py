'''
@Author 浊玉
@Description  
@Date create in 2023/5/26 19:30
'''

str1 = '桂林航天工业学院计算机科学与工程学院2022级物联网工程专业x班，学号xxxx，姓名xx'
# 写入文件 info.txt 这里用到了with的文本管理
with open(r'info.txt', 'a', encoding='utf-8') as file:
    file.write(str1)

print("追加写入完成！")
# 从文件读取信息
with open(r'./info.txt', 'r', encoding='utf-8') as file:
    print(file.read())
