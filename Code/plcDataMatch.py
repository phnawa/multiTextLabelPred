import difflib
import pandas as pd
from plcDataMerge import plcMerge
from plcDataProcess import plcProcessing, plcTestProcessing
from plcDataTokenization import plcFenci, plcTestFenci
from fenciPad import plcPadding, plcTestPadding
import os


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


def plcAdd(inputPath, outputPath):

    inputPath = inputPath.rsplit('.')[-2]
    outputPath = outputPath.rsplit('.')[-2]

    path = os.getcwd()
    plcTestProcessing(inputPath)
    plcTestFenci(inputPath)
    plcTestPadding(inputPath)

    plcMerge()
    plcProcessing()
    plcFenci()
    plcPadding()

    TestData = pd.read_csv(inputPath + '.csv')
    TestData = TestData.loc[:,['Name']]
    RawDataMerge = pd.read_csv(path + '//Files//plcMappingMerge.csv')
    RawDataProcess = pd.read_csv(path + '//Files//plcMappingProcess.csv')
    RawDataProcess_label = RawDataProcess['Category']
    
    with open(inputPath + 'FenciPad2.txt', "r") as f:
        #测试数据的fenciPad2表
        TestDataFenciPad2 = f.readlines()
    
    PredIdx, idlist = [], []
    for w in range(len(TestData['Name'])):
    #经典匹配
        idlist.append(w+1)
        if TestData.at[w, 'Name'] in RawDataMerge['Name'].values:
            TestData.at[w, 'Mechanism'] = RawDataMerge[RawDataMerge['Name'] == TestData.at[w, 'Name']].iloc[0,1]
            TestData.at[w, 'Components'] = RawDataMerge[RawDataMerge['Name'] == TestData.at[w, 'Name']].iloc[0,2]
            TestData.at[w, 'InnerMonitoring'] = RawDataMerge[RawDataMerge['Name'] == TestData.at[w, 'Name']].iloc[0,3]
            TestData.at[w, 'Similarity'] = 1
        else:
            #分词匹配
            TestDataFenciPad2[w] = TestDataFenciPad2[w].strip('\n').split() 
            sv = []
            for v in range(len(RawDataProcess_label)):

                RawDataProcess_label[v] = RawDataProcess_label[v].replace('[', '').replace(']', '')\
                    .replace(',', '').replace('\'', '').replace(' ','')
                
                sv.append(string_similar(''.join(TestDataFenciPad2[w]), ''.join(RawDataProcess_label[v])))
            idx = sv.index(max(sv))
            #print(''.join(TestDataFenciPad2[w]), '------------', ''.join(RawDataProcess_label[idx]), '------------', max(sv))
            TestData.at[w, 'Mechanism'] = RawDataMerge.at[idx, 'Mechanism']
            TestData.at[w, 'Components'] = RawDataMerge.at[idx, 'Components']
            TestData.at[w, 'InnerMonitoring'] = RawDataMerge.at[idx, 'InnerMonitoring']
            TestData.at[w, 'Similarity'] = max(sv)
            PredIdx.append(w+2)

    #TestData =TestData.sort_values(by='Similarity')
    TestData.insert(loc=0, column='id', value=idlist)
    TestData['id'] = TestData['id'].astype(int)
    TestData.to_csv(outputPath + '.csv', index=False)

    os.remove(path + '//Files//plcMappingMerge.csv')
    os.remove(path + '//Files//plcMappingProcess.csv')
    os.remove(inputPath + 'Process.csv')

    os.remove(path + '//Files//plcMappingProcess.txt')
    os.remove(path + '//Files//plcMappingFenci.txt')
    os.remove(path + '//Files//plcMappingFenciPad.txt')
    os.remove(path + '//Files//plcMappingFenciPad2.txt')
    os.remove(inputPath + 'Process.txt')
    os.remove(inputPath + 'Fenci.txt')
    os.remove(inputPath + 'FenciPad.txt')
    os.remove(inputPath + 'FenciPad2.txt')

