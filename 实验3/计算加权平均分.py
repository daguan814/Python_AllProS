
'''
@Author 浊玉
@Description  冒泡排序
@Date create in 2023/5/12 12:24
'''

n = int(input("请输入修读课程的门数："))

# 初始化总成绩和总学分
total_grade = 0
total_credit = 0

stu = []

# 输入每门课的名称、成绩和学分，并累加总成绩和总学分
for i in range(n):
    course_name = input("请输入第%d门课的名称：" % (i+1))
    grade = int(input("请输入第%d门课的成绩：" % (i+1)))
    credit = int(input("请输入第%d门课的学分：" % (i+1)))
    total_grade += grade * credit
    total_credit += credit
    stu.append('名称：'+course_name + '成绩：'+str(grade) + '学分：'+str(credit))

# 计算加权平均分
weighted_average = total_grade / total_credit
print(stu)
# 输出结果
print("加权平均分为：%.2f" % weighted_average)
