'''
@Author 浊玉
@Description
@Date create in 2023/10/10 19:58
'''
import time
from Tools import Tools

tools = Tools()
# 使用示例

# file_path = input('请拖入学生名单：')
file_path = '考号处理.xlsx'  # 替换成你的Excel文件路径
Class_Stu = tools.excel_to_2d_array(file_path)  # 班级人名对照表
'''--------------------'''
KaoChang_RenShu = [30, 30, 30, 30, 30, 40, 40, 40, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 0]  # 考场人数对照表
KaoChang_Stu = [[] for _ in range(70)]
for ii in range(70):
    KaoChang_Stu[ii] = [' ' for _ in range(70)]  # 考场学生对照表

kaochang = 0  # 现在填充的考场号
banji = 1  # 现在的班级
tmp = 0
count_kao = KaoChang_RenShu[kaochang]  # 考场统计人数
index = None
for i in range(0, 10000):
    while True:
        if banji == 50:  # 所有班级的学生都放入考场了
            print(KaoChang_Stu)
            tools.save_to_excel(KaoChang_Stu, '考场表.xlsx')
            kaohao_arr = tools.write_to_kaohao(KaoChang_Stu)
            kaohao_arr = tools.remove_empty_first_column_rows(kaohao_arr)
            tools.save_to_excel(kaohao_arr, '考号表.xlsx')
            print(kaohao_arr)
            time.sleep(2)
            exit()
        #     break  # 如果班级到达14，直接结束程序
        index = tools.find_first_stu(Class_Stu, banji)
        if index == 9999:  # 某个班的学生全部都放入考场了
            banji += 1
        else:
            break
    print(index)
    KaoChang_Stu[tmp][kaochang] = Class_Stu[index][1]  # 将学生放入考场
    Class_Stu.pop(index)  # 将这个学生删除
    banji += 1
    tmp += 1
    if banji > 14:  # 班级数
        banji = 1
    if i == count_kao - 1:
        kaochang += 1
        tmp = 0
        count_kao = count_kao + KaoChang_RenShu[kaochang]
