import pandas as pd
import os



def plcMerge():

    path = os.getcwd()
    plc = pd.read_excel(path + '//Files//plcMapping.xlsx', sheet_name=None)
    plc_Merge = pd.DataFrame()
    for i in range(len(plc.keys())):
        plc1= pd.read_excel(path + '//Files//plcMapping.xlsx', index_col=None, header=0, 
                        sheet_name=i, usecols="A:D")
        plc_Merge = pd.concat([plc_Merge, plc1], axis=0, ignore_index=True)

    #去除标签全为‘略’的行
    sums = (plc_Merge=="略").astype(int).sum(axis=1)
    sums_result = list(sums[sums>2].index)
    plc_Merge = plc_Merge.drop(sums_result,axis=0)
    plc_Merge = plc_Merge.reset_index(drop=True)
    plc_Merge.to_excel(path + '//Files//plcMappingMerge.xlsx', index=False)