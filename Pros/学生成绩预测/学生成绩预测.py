#!/usr/bin/env python
# coding: utf-8

'''
属性信息：
学校 - 学生的学校（二进制："GP" - 加布里埃尔·佩雷拉或"MS" - 穆西尼奥·达·西尔维拉）
性别 - 学生的性别（二进制："F"-女性或"M"-男性）
年龄 - 学生的年龄（数字：从15岁到22岁）
地址 - 学生的家庭住址类型（二进制："U"- 城市或"R" - 农村）
famsize - 系列大小（二进制："LE3" - 小于或等于 3 或 "GT3" - 大于 3）
Pstatus - 父母的同居状态（二进制："T" - 生活在一起或"A" - 分开）
Medu - 母亲教育（数字：课堂实验 - 无，1 - 小学教育（4年级），2 - 5至9年级，3 - 中学教育或4 - 高等教育）
fadu- 父亲的教育（数字：课堂实验 - 无，1 - 小学教育（4年级），2 - 5至9年级，3 - 中等教育或4 - 高等教育）
Mjob - 母亲的工作（名义上："教师"，"健康"护理相关，民事"服务"（例如行政或警察），"at_home"或"其他"）
Fjob - 父亲的工作（名义上："教师"，"健康"护理相关，民事"服务"（例如行政或警察），"at_home"或"其他"）
原因 - 选择这所学校的原因（名义上：接近"家"，学校"声誉"，"课程"偏好或"其他"）
监护人 - 学生的监护人（名义上："母亲"、"父亲"或"其他"）
旅行时间 - 从家到学校的旅行时间（数字：1 - <15 分钟、2 - 15 至 30 分钟、3 - 30 分钟至 1 小时，或 4 - >1 小时）
学习时间 - 每周学习时间（数字：1 - <2小时，2 - 2至5小时，3 - 5至10小时，或4 - >10小时）
失败 - 过去类失败的次数（如果 1<=n<3，则为数字：n，否则为 4）
学校 - 额外的教育支持（二进制：是或否）
famsup - 家庭教育支持（二进制：是或否）
付费 - 课程科目（数学或葡萄牙语）内的额外付费课程（二进制：是或否）
活动 - 课外活动（二进制：是或否）
托儿所 - 就读的托儿所（二进制：是或否）
更高 - 想接受高等教育（二进制：是或否）
互联网 - 在家访问互联网（二进制：是或否）
浪漫 - 有浪漫的关系（二进制：是或否）
家庭 - 家庭关系的质量（数字：从1 - 非常糟糕到5 - 优秀）
空闲时间 - 放学后的空闲时间（数字：从1 - 非常低到5 - 非常高）
外出 - 与朋友一起外出（数字：从1 - 非常低到5 - 非常高）
Dalc - 工作日饮酒量（数字：从1 - 非常低到5 - 非常高）
Walc - 周末饮酒量（数字：从1 - 非常低到5 - 非常高）
运行状况 - 当前运行状况（数字：从 1 - 非常糟糕到 5 - 非常好）
缺勤 - 缺课次数（数字：从0到93）
这些成绩与课程科目，数学或葡萄牙语相关：
G1 - 第一期等级（数字：从0到20）
G2 - 第二阶段等级（数字：从0到20）
G3 - 最终等级（数字：从0到20，输出目标）

特征工程后保存：[["Medu",  "traveltime", "studytime", "famrel", "Dalc",  "health", "absences", "G1", "G2"]]
'''

# In[2]:


# 将数据加入环境变量
import os

import matplotlib.pyplot as plt
# 数据分析的目的是通过使用一些与G3相关的参数，选择合适的方法来预测学生在第三阶段的成绩。
# 导入必要的库
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# In[3]:

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# In[5]:


data = pd.read_csv('student-mat.csv')  # 数据存放的地址

# In[6]:


data.head  # 读取数据

# In[7]:


data.columns  # 数据的列

# In[8]:


# 数据处理

# 我们需要通过G1、G2、健康状况、缺勤等数据来预测G3的等级。

# 我们将决定哪些列我们需要设置为功能

# 我们根据常识选择的功能是“Medu”、“Fedu”、“traveltime”、“studytime”、“famrel”、“Dalc”、“Walc”、“health”、“absences”、“G1”和“G2”

# 设置这些列为x
x = data[["Medu", "Fedu", "traveltime", "studytime", "famrel", "Dalc", "Walc", "health", "absences", "G1", "G2"]]
print(x)

# In[9]:


x.head  # 显示数据

# In[10]:


y = data["G3"]  # y是要预测的数据
print(y.head())  # 输出y

# In[11]:


# 检查数据是否包含 Nan 值
na_cols = data.isna().any()
na_cols = na_cols[na_cols == True]
print(na_cols)
# 原来数据无空值


# In[12]:


m = y.value_counts().sort_values()
print(m)  # 统计G3

# In[13]:


# 绘制一些图片来标记可能影响 g3的因素之间的关系
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["Medu"], y, width=0.5)
plt.show()
# 数据表明：他们母亲的教育水平越高，学生在三年内能达到的年级就越高。


# In[14]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["Fedu"], y, width=0.5)
plt.show()
# 父亲受教育水平与母亲的有相似之处，但是关系并不明显


# In[15]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["traveltime"], y, width=0.5)
plt.show()
# 旅行的时间越短 成绩越好


# In[16]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["studytime"], y, width=0.5)
plt.show()
# 不同学习时间可能会导致成绩不同，但是关系不明显


# In[17]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["famrel"], y, width=0.5)
plt.show()
# 家庭关系会影响学生学习，对其产生较大影响


# In[18]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["Dalc"], y, width=0.5)
plt.show()

# In[19]:


# 学生成绩与喝酒时间的比较
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["Walc"], y, width=0.5)
plt.show()

# In[20]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["Dalc"], y, width=0.5)
plt.show()
# 学生在上课期间（周一至周五）喝酒反而有助于成绩 周末喝酒对成绩影响不大


# In[21]:


plt.figure(figsize=(20, 8), dpi=100)
plt.scatter(data["health"], y)
plt.show()
# 健康水平为2的学生学习更好


# In[22]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["absences"], y, width=0.5)
plt.show()
# 旷课越少，成绩越好


# In[23]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["G1"], y, width=0.5)
plt.show()
# 第一阶段分数高的学生第三阶段也高


# In[24]:


plt.figure(figsize=(20, 8), dpi=100)
plt.bar(data["G2"], y, width=0.5)
plt.show()
# 第二阶段分数高 第三阶段也高


# In[25]:


# 经过分析排除学校上课喝酒和父亲受教育程度对学生成绩的影响
x_new = x.drop(["Walc", "Fedu"], axis=1)
print(x_new.head())

# In[26]:


# 构建机器学习模型
# 数据集划分
x_train, x_test, y_train, y_test = train_test_split(x_new, y, random_state=6)

transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# In[27]:


estimator = RandomForestClassifier(n_estimators=10, criterion="entropy", max_depth=8, bootstrap=True,
                                   max_features="auto")
estimator.fit(x_train, y_train)
y_predict = estimator.predict(x_test)
accuracy = estimator.score(x_test, y_test)
print("随机森林算法:\n", accuracy)

# In[31]:


estimator = LinearRegression(fit_intercept=True)
estimator.fit(x_train, y_train)
print(estimator.coef_)
print(estimator.intercept_)
y_predict = estimator.predict(x_test)
print("线性回归预测的数值：\n", y_predict)
print("线性回归预测准确:\n", accuracy)

# In[40]:


estimator = Ridge(alpha=1, max_iter=10000)
estimator.fit(x_train, y_train)
print(estimator.coef_)
print(estimator.intercept_)
y_predict = estimator.predict(x_test)
print("岭回归预测数值：：\n", y_predict)
accuracy = estimator.score(x_test, y_test)
print("岭回归准确:\n", accuracy)

# In[58]:


# 使用网格搜索 找到最佳的岭回归参数
param_dict = {"alpha": [0.5, 0.6, 0.7, 0.8, 0.9, 1], "max_iter": [10000, 50000, 100000, 150000, 200000]}
estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
estimator.fit(x_train, y_train)
print("最佳参数:\n", estimator.best_params_)
print("最佳预估器：\n", estimator.best_estimator_)
print("最高分:\n", estimator.best_score_)

'''
本次课题数据来源：kaggle.com

研究目标：对葡萄牙学生的第三阶段成绩的预测  （葡萄牙学生学习共三个阶段 
相当于中国三个学年）

特征工程：未采用降维的方法减少特征个数 ，根据数据表格的直观分析和日常生活的理论对数据进行了特征减少

本次研究结果：使用岭回归算法可以得到最高83%的预测准确率

总结：对于葡萄牙学生来说第一第二阶段的成绩对学生第三阶段成绩影响很大
家庭关系对学生学习影响也比较大
母亲的文化水平对学生成绩也有一定的影响



# In[xx]:
#最终验证(已弃用)
[["Medu",  "traveltime", "studytime", "famrel", "Dalc",  "health", "absences", "G1", "G2"]]

Medu - 母亲教育（数字：课堂实验 - 无，1 - 小学教育（4年级），2 - 5至9年级，3 - 中学教育或4 - 高等教育）
旅行时间 - 从家到学校的旅行时间（数字：1 - <15 分钟、2 - 15 至 30 分钟、3 - 30 分钟至 1 小时，或 4 - >1 小时）
学习时间 - 每周学习时间（数字：1 - <2小时，2 - 2至5小时，3 - 5至10小时，或4 - >10小时）
失败 - 过去类失败的次数（如果 1<=n<3，则为数字：n，否则为 4）
Dalc - 工作日饮酒量（数字：从1 - 非常低到5 - 非常高）
运行状况 - 当前运行状况（数字：从 1 - 非常糟糕到 5 - 非常好）
缺勤 - 缺课次数（数字：从0到93）
G1 - 第一期等级（数字：从0到20）
G2 - 第二阶段等级（数字：从0到20）
G3 - 最终等级（数字：从0到20，输出目标）



'''

x12 = [[5, 1, 1, 1, 1, 1, 1, 1, 15]]
x12 = transfer.fit_transform(x12)
estimator = Ridge(alpha=1, max_iter=10000)
estimator.fit(x_train, y_train)
y_predict = estimator.predict(x12)
print(y_predict)
