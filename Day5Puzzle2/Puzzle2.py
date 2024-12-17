from os.path import dirname
def sum_unordered_pagenumbers(page_lists:list[list[int]], rules:list[str]) -> int:

    def is_ordered(page:int, lower:list[int]) -> bool:
        return all([True if (("%d|%d" % (i,page)) in (rules)) else False for i in lower])
    
    total = 0
    unordered_page_lists =  [pages for pages in page_lists if not(all([is_ordered(pages[j], pages[0:j]) for j in range(1,len(pages)-1)]))]
    rules_formatted = [[int(x), int(y)] for x, y in [a.split("|") for a in rules]]
    
    for pages in unordered_page_lists:
        page_rule_lower_pairs = [x[0] for x in list(filter(lambda y: (y[0] in pages and y[1] in pages), rules_formatted))]
        total += {page_rule_lower_pairs.count(i):i for i in pages}[len(pages) // 2]
        
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
            
    x = sum_unordered_pagenumbers(page_lists, rules)
    # print(x)
    return x
    
if __name__ == "__main__":
    main()