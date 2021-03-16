# 分词器 v1:分词与初步清除（特殊符号）
# 分词器 v2:停用词去除
import jieba
import jieba.analyse
import codecs
import re


# 停用词
def stopwordslist():
    stopwords = [line.strip() for line in open('../stopwords-master/hit_stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords


# 文章分词
def cut_words(sentence):
    # print sentence
    return " ".join(jieba.cut(sentence)).encode('utf-8')


# 文件路径
f = codecs.open('../texts/text_tmall.txt.txt', 'r', encoding="utf8")  # 打开要分词的文件
target = codecs.open("../texts/text_tmall_cut.txt", 'w', encoding="utf8")  # 最终分词好的文本存储的地址
# 逐行分词处理
print('open files')
line_num = 1
# 逐行迭代器
line = f.readline()
while line:
    line_seg = " ".join(jieba.cut(line))  # jieba分词一排文本
    # line_seg_new = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+", " ", line_seg)
    stopwords = stopwordslist()
    line_seg_new=''
    for word in line_seg:
        if word not in stopwords:
            if word != '\t':
                line_seg_new+= word
                line_seg_new+= " "
                print("去除停用词")
    target.writelines(line_seg_new)  # 写入到目标文件中
    # target.writelines('\n')
    line_num = line_num + 1
    line = f.readline()
