from os.path import dirname

def count_crossover_tokens(wordsearch:list[str], key) -> int:
    totals = 0
    if (len(key) == 1 or len(key) % 2 == 0): return 0
    checker = [key,key[::-1]]
    middle_letter_index = (len(key) // 2)
    middle_letter = key[middle_letter_index]
    crossover_letter_coordinates = [[x,y] for x in range(middle_letter_index,len(wordsearch)-(middle_letter_index)) 
                                          for y in range(middle_letter_index,len(wordsearch[0])-(middle_letter_index))
                                    if wordsearch[x][y] == middle_letter]
    for i in crossover_letter_coordinates:
        diagonal1, diagonal2 = '', ''
        for j in range(-middle_letter_index,middle_letter_index+1):
            diagonal1 += wordsearch[i[0]+j][i[1]+j] # english
            diagonal2 += wordsearch[i[0]+j][i[1]-j] # hebrew
        if(diagonal1 in checker and diagonal2 in checker): totals += 1
        
    return totals

def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day4Dataset.txt'
    wordsearch = []
    with open(data_file_path,'r') as file:
        for row in file:
            wordsearch.append(row.replace('\n',''))
            
    x = count_crossover_tokens(wordsearch, 'MAS')
    # print(x)
    return x
    
if __name__ == "__main__":
    main()