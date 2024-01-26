import pandas as pd
import jieba
import jieba.analyse
import os


def plcFenci():

    PATH = os.getcwd()
    jieba.load_userdict(PATH + '//Files//userDict.txt')
    df = pd.read_excel(PATH + '//Files//plcMappingProcess.xlsx')
    df1 = df['Name']
    df1.to_csv(PATH + '//Files//plcMappingProcess.txt', header=None, sep=',', index=False)


    txt = open(PATH + '//Files//plcMappingProcess.txt',encoding='utf-8').read()
    count  = jieba.cut(txt, cut_all=False, HMM=True)

    f=open(PATH + '//Files//plcMappingFenci.txt', 'w')
    for line in count:
        for a in line:
            f.write(a)
        f.write(' ')
    f.close()


def plcTestFenci(path):

    PATH = os.getcwd()
    jieba.load_userdict(PATH + '//Files//userDict.txt')
    df = pd.read_excel(path + 'Process.xlsx')
    df1 = df['Name']
    df1.to_csv(path + 'Process.txt', header=None, sep=',', index=False)


    txt = open(path + 'Process.txt',encoding='utf-8').read()
    count  = jieba.cut(txt, cut_all=False, HMM=True)

    f=open(path + 'Fenci.txt', 'w')
    for line in count:
        for a in line:
            f.write(a)
        f.write(' ')
    f.close()        