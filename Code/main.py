from plcDataMatch import plcAdd
import sys


if __name__ == "__main__":

    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    plcAdd(inputPath, outputPath)