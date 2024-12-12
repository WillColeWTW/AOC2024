from os.path import dirname

def sumOfDifferences(filePath:str) -> int:
    LocationIdList1 = []
    LocationIdList2 = []
    
    with open(filePath,'r') as data:
        for row in data:
            row = row.replace('\n','')
            x, y = row.split(',')
            LocationIdList1.append(int(x))
            LocationIdList2.append(int(y.replace('\n','')))
    
    LocationIdList1.sort(); LocationIdList2.sort();
    return sum([abs(x - y) for x, y in zip(LocationIdList1,LocationIdList2)])

def main():
    # puzzle 1
    currentPath = dirname(__file__)
    dataListFile = currentPath + '\\Puzzle1Datasets.csv'
    x = sumOfDifferences(dataListFile)
    # print(x)
    return x
       
if __name__ == "__main__":
    main()