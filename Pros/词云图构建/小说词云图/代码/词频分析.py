# -*- coding: utf-8 -*-


import re
import jieba as jb


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence = re.sub(u'[0-9\.]+', u'', sentence)

    jb.add_word('今年')  # 这里是加入用户自定义的词来补充jieba词典。
    jb.add_word('成为')  # 如果你想删除哪个特定的词，就先把它加上然后放进停用词表里。

    sentence_seged = jb.cut(sentence.strip())
    # stopwords = pd.read_csv("./stopwords.txt", index_col=False, quoting=3, sep=" ", names=['stopword'],
    #                         encoding='UTF-8')
    stopwords = stopwordslist('./stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords and word.__len__() > 1:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# 这里要注意编码问题 inputs即是读入原文本，outputs即是新建一个文本，然后将处理好的文本放入
print("开始分析---")
inputs = open(r'./三国.txt', 'r', encoding='utf-8')

outputs = open(r'./输出/output_data.txt', 'w', encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

print("分析完成!")
