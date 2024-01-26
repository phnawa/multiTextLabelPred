import pandas as pd
import jieba
import jieba.analyse
import os

path = os.getcwd()

jieba.load_userdict('./Files/userDict.txt')

def fenci(rawData):
    df = pd.read_excel(path + '//Files//' + rawData + 'Process.xlsx')
    df1 = df['Name']
    df1.to_csv(path + '//Files//' + rawData + 'Process.txt', header=None, sep=',', index=False)


    txt = open(path + '//Files//' + rawData + 'Process.txt',encoding='utf-8').read()
    count  = jieba.cut(txt, cut_all=False, HMM=True)

    f=open(path + '//Files//' + rawData + 'Fenci.txt', 'w')
    for line in count:
        for a in line:
            f.write(a)
        f.write(' ')
    f.close()