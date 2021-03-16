# -*- coding: UTF-8 -*-

import jieba
import jieba.analyse
import codecs

'''
    把jieba分词好的文本输入到txt文件中保存起来
    这样以后可以直接输入到Doc2vec中训练了，降低了处理语料库和doc2vec模型的耦合度
'''

#文章分词
def cut_words(sentence):
   #print sentence
    return " ".join(jieba.cut(sentence)).encode('utf-8')

f=codecs.open('E:\WIKI_Data\cuted_WIKI_DATA\wiki.zh.jian_15.txt','r',encoding="utf8")#打开要分词的文件
target = codecs.open("E:\WIKI_Data\jiebaed_wiki.zh.jian_15.txt", 'w',encoding="utf8")#最终分词好的文本存储的地址

print ('open files')
line_num=1#当前正在处理的是第几排文章（一排一篇文章）
line = f.readline()#line现在是个迭代器
while line:#开始一行一行地读取文本，总共有239023篇文章，即239023排
    if(line_num%1000  == 1):
        # 每隔1000条文本就打印一下进度
        print('---- processing', line_num, 'article----------------')
    line_seg = " ".join(jieba.cut(line))# jieba分词一排文本
    target.writelines(line_seg)#写入到目标文件中
    line_num = line_num + 1
    line = f.readline()# 该方法每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。
print('处理结束')