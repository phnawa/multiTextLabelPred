import pandas as pd
import os

path = os.getcwd()

def plcDataProcessing(rawData):
    
    data = pd.read_excel(path + '//Files//' + rawData + '.xlsx')

    if data.shape[1] > 1:
        merge_data = pd.read_excel(path + '//Files//' + rawData + 'Merge.xlsx')
        merge_data.loc[:,'Category'] = ""
        for i in range(merge_data.shape[0]):
            if str(merge_data.at[i,'Mechanism'])!='nan':
                merge_data.at[i,'Category'] += str(merge_data.at[i,'Mechanism'])
            if str(merge_data.at[i,'Components'])!='nan':
                merge_data.at[i,'Category'] += ',' + str(merge_data.at[i,'Components'])
            if str(merge_data.at[i,'InnerMonitoring'])!='nan':
                merge_data.at[i,'Category'] += ',' + str(merge_data.at[i,'InnerMonitoring'])
            merge_data.at[i,'Category'] = merge_data.at[i,'Category'].split(',')
            merge_data.at[i, 'Name'] = merge_data.at[i, 'Name'].replace('#', '号')
        merge_data.drop(['Mechanism', 'Components', 'InnerMonitoring'], axis=1, inplace=True)
        merge_data.to_excel(path + '//Files//' + rawData + 'Process.xlsx', index=False)

    else:        
        for i in range(data.shape[0]):
            data.at[i, 'Name'] = data.at[i, 'Name'].replace('#', '号')
        data.to_excel(path + '//Files//' + rawData + 'Process.xlsx', index=False)