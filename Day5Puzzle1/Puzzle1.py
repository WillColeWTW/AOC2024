from os.path import dirname

def sum_ordered_pagnumbers(page_lists:list[list[int]], rules:list[str]) -> int:
    total = 0
    def is_ordered(page:int, lower:list[int], upper:list[int]) -> bool:
        a, b = True, True
        if(len(lower) > 0): a = all([True if (("%d|%d" % (i,page)) in (rules)) else False for i in lower])
        if(len(upper) > 0): b = all([True if (("%d|%d" % (page,i)) in (rules)) else False for i in upper])
        return a and b
    for pages in page_lists:
        if all([is_ordered(pages[j], pages[0:j], pages[(j+1):len(pages)]) for j in range(0,len(pages))]):
            total += pages[(len(pages) // 2)]
    return total

def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day5Dataset.txt'
    rules = []; page_lists = []; 
    is_page_pairs = True;
    
    with open(data_file_path,'r') as file:
        for row in file:
            if row == '\n': 
                is_page_pairs = False
                continue
            if(is_page_pairs):
                rules.append(row.replace('\n',''))
            else:
                page_lists.append(list(map(int, row.replace('\n','').split(','))))
            
    x = sum_ordered_pagnumbers(page_lists, rules)
    # print(x)
    return x
    
if __name__ == "__main__":
    main()