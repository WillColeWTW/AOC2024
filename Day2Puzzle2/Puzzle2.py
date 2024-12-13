from os.path import dirname

def count_safe_enough_levels(report_list:list[list[int]]) -> int:

    def is_safe(report: list[int]) -> bool:
        difference_list = [report[i] - report[i-1] for i in range(1,len(report))]
        return all([abs(i) < 4 for i in difference_list]) and len(set([1 if i > 0 else -1 if i < 0 else 0 for i in difference_list])) == 1
    
    def is_safe_enough(report: list[int]) -> bool:
        if(is_safe(report)):
            return True
        if any([is_safe(report[0:(j-1)]+report[j:len(report)]) for j in range(1,len(report)+1)]):
            return True
        return False
    
    return [is_safe_enough(i) for i in report_list].count(True)
            

def main():
    
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day2Dataset.txt'
    
    report_lists = []
    
    with open(data_file_path,'r') as data:
        for row in data:
            row = row.replace('\n','')
            report_lists.append(list(map(int, row.split(' '))))
    
    # puzzle 2
    x = count_safe_enough_levels(report_lists)
    # print(x)
    return x
       
if __name__ == "__main__":
    main()