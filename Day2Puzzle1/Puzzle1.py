from os.path import dirname
from typing import List

'''
A report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''
def count_safe_levels(report_list:List[List[int]]) -> int:

    def is_safe(report: List[int]) -> bool:
        difference_list = [report[i] - report[i-1] for i in range(1,len(report))]
        return all([abs(i) < 4 for i in difference_list]) and len(set([1 if i > 0 else 0 for i in difference_list])) == 1
    
    return len(list(filter(is_safe, report_list)))

def main():
    
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Puzzle1Datasets.txt'
    
    report_lists = []
    
    with open(data_file_path,'r') as data:
        for row in data:
            row = row.replace('\n','')
            report_lists.append(list(map(int, row.split(' '))))
    # puzzle 1
    x = count_safe_levels(report_lists)
    print(x)
    return x
       
if __name__ == "__main__":
    main()