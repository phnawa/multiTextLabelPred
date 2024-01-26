import pandas as pd
import os



def plcProcessing():
    
    path = os.getcwd()
    merge_data = pd.read_excel(path + '//Files//plcMappingMerge.xlsx')
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
    merge_data.to_excel(path + '//Files//plcMappingProcess.xlsx', index=False)


def plcTestProcessing(path):

    merge_data = pd.read_excel(path + '.xlsx')       
    for i in range(merge_data.shape[0]):
        merge_data.at[i, 'Name'] = merge_data.at[i, 'Name'].replace('#', '号')
    merge_data.to_excel(path + 'Process.xlsx', index=False)