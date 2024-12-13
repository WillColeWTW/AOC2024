from os.path import dirname

def count_all_tokens(wordsearch:list[str],key) -> int:
    
    def count_tokens_forward_and_down(wordsearch:list[str],key) -> int:
        token_count = sum([i.count(k) for i in wordsearch for k in [key,key[::-1]]])
        for i in range(len(key),(len(wordsearch)+len(wordsearch[0])-len(key))):
            entry = []
            for x in range(0,len(wordsearch[0])):
                if (i-x) > -1 and (i-x) < len(wordsearch):
                    entry.append(wordsearch[i-x][x])
            # print(entry)
            token_count += sum(["".join(entry).count(k) for k in [key,key[::-1]]])
        return token_count
    
    return sum([count_tokens_forward_and_down(x, key) for x in [wordsearch, ["".join(list(i)) for i in zip(*wordsearch[::-1])]]])
    
def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day4DatasetSample.txt'
    wordsearch = []
    with open(data_file_path,'r') as file:
        for row in file:
            wordsearch.append(row.replace('\n',''))
            
    x = count_all_tokens(wordsearch, 'XMAS')
    # print(x)
    return x
    
if __name__ == "__main__":
    main()