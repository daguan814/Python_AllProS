from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd

print("开始绘图")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = True  # 正常显示负号

with open("./output_data.txt", encoding='utf-8') as f:
    conlist = f.read()

# image = np.array(Image.open(r'./成果/词云图/2.png'))
sw = set(STOPWORDS)
sw.add("【")
sw.add("】")
sw.add("/")
sw.add("")

# STOPWORDS='./停用词库.txt'
wc = WordCloud(stopwords=sw,
               font_path=r'./Arial Unicode.ttf',
               collocations=False,
               background_color='white',
               width=800,
               height=600)  # 设置词云图的参数，字体，高度宽度和背景颜色等
con = wc.generate(conlist)

wc.to_file(r"./词云图.png")

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
df2 = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:30]  # ('发展', 217)格式

dff = pd.DataFrame(df2)
dff.to_csv(r'./词频统计.csv')

print("分析完成")
