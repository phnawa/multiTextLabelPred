import pandas as pd
import os


def plcPadding():

    path = os.getcwd()
    rely_Table = pd.read_csv(path + '//Files//relyTable.txt', sep=' ', header=None)
    replace_Table = pd.read_csv(path + '//Files//replaceTable.txt', sep=' ', header=None)

    fw = open(path + '//Files//plcMappingFenciPad.txt', 'w')

    with open(path + '//Files//plcMappingFenci.txt', "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split() 
            for v in range(len(line)):
                if line[v] in rely_Table.iloc[:,0].to_list():
                    line.append(rely_Table.iloc
                                [rely_Table.iloc[:,0].tolist().index(line[v]),1])
                break
            fw.write(' '.join(line))
            fw.write('\n')
    fw.close()

    fw = open(path + '//Files//plcMappingFenciPad2.txt', 'w')

    with open(path + '//Files//plcMappingFenciPad.txt', "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split() 
            for v in range(len(line)):
                if line[v] in replace_Table.iloc[:,0].to_list():
                    instead = replace_Table.iloc[replace_Table.iloc[:,0].tolist().index(line[v]),1]
                    if instead == '0':
                        line[v] = ''
                    else:
                        line[v] = instead
            fw.write(' '.join(line))
            fw.write('\n')
    fw.close()


def plcTestPadding(path):
    
    PATH = os.getcwd()
    rely_Table = pd.read_csv(PATH + '//Files//relyTable.txt', sep=' ', header=None)
    replace_Table = pd.read_csv(PATH + '//Files//replaceTable.txt', sep=' ', header=None)

    fw = open(path + 'FenciPad.txt', 'w')

    with open(path + 'Fenci.txt', "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split() 
            for v in range(len(line)):
                if line[v] in rely_Table.iloc[:,0].to_list():
                    line.append(rely_Table.iloc
                                [rely_Table.iloc[:,0].tolist().index(line[v]),1])
                break
            fw.write(' '.join(line))
            fw.write('\n')
    fw.close()

    fw = open(path + 'FenciPad2.txt', 'w')

    with open(path + 'FenciPad.txt', "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split() 
            for v in range(len(line)):
                if line[v] in replace_Table.iloc[:,0].to_list():
                    instead = replace_Table.iloc[replace_Table.iloc[:,0].tolist().index(line[v]),1]
                    if instead == '0':
                        line[v] = ''
                    else:
                        line[v] = instead
            fw.write(' '.join(line))
            fw.write('\n')
    fw.close()    