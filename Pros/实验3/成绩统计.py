
'''
@Author 浊玉
@Description  冒泡排序
@Date create in 2023/5/12 12:30
'''

import statistics

scores = []
count = 0

while count < 10:
    try:
        score = int(input(f"请输入第{count + 1}个成绩："))
        if score < 0 or score > 100:
            print("请输入0-100的整数！")
        else:
            scores.append(score)
            count += 1
    except ValueError:
        print("请输入0-100的整数！")

average = statistics.mean(scores)  #statistics模块中的函数来计算平均值、标准差和中位数。
std_dev = statistics.stdev(scores)
median = statistics.median(scores)
pass_rate = sum(score >= 60 for score in scores) / len(scores)

print(f"平均值：{average:.1f}")
print(f"标准差：{std_dev:.1f}")
print(f"中位数：{median:.1f}")
print(f"及格率：{pass_rate:.1%}")
