from plcDataMatch import plcAdd
import sys
import getopt


if __name__ == "__main__":

    rawData = 'plcMapping'
    testData = 'plcTest'
    generateData = 'plcTestDataPred'

    plcAdd(rawData, testData, generateData)