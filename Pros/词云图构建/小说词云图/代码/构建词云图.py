from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

print("开始绘图")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = True  # 正常显示负号

with open("./输出/output_data.txt", encoding='utf-8') as f:
    conlist = f.read()


sw = set(STOPWORDS)  #这里可以添加  ②统计次数和词云生成中去掉排名靠
# 前但是非人物名字的词 也可以在stopwords.txt中添加
sw.add("人马")
sw.add("")
sw.add("/")
sw.add("")


wc = WordCloud(stopwords=sw,
               font_path=r'./字体文件/Arial Unicode.ttf',
               collocations=False,
               background_color='white',
               width=800,
               height=600)  # 设置词云图的参数，字体，高度宽度和背景颜色等
con = wc.generate(conlist)

wc.to_file(r"./输出/词云图.png")

# 词频统计的三种方法 先准备好数据的形式为列表形式
# 对于txt格式中读入的文件，先把它放进列表中
all_data = conlist.split(' ')

# N0.1 使用pandas进行词频统计
df2 = pd.Series(all_data).value_counts().head(30)  # array格式，转成DataFrame再保存csv

# N0.2 导入相关库
from collections import Counter

wordcount = Counter(all_data)
df2 = wordcount.most_common(30)  # ('发展', 217) 格式

# N0.3
wordcount = {}
for word in all_data:
    wordcount[word] = wordcount.get(word, 0) + 1
df2 = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:30]

dff = pd.DataFrame(df2)
dff.to_csv(r'./输出/词频统计.csv')

print("分析完成")
