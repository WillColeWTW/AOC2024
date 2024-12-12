from os.path import dirname
from typing import List


def similarity_score(location_list_one:List[int], location_list_two:List[int]) -> int:
    referenced_location_frequencies = {x: location_list_two.count(x) for x in location_list_two if x in location_list_one}
    return sum([x * referenced_location_frequencies[x] for x in referenced_location_frequencies.keys()])

def main():
    
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Puzzle1Datasets.csv'
    
    location_list_one = []
    location_list_two = []
    
    with open(data_file_path,'r') as data:
        for row in data:
            row = row.replace('\n','')
            x, y = row.split(',')
            location_list_one.append(int(x))
            location_list_two.append(int(y.replace('\n','')))
    
    # puzzle 2
    x = similarity_score(location_list_one, location_list_two)
    print(x) # 26407426
    return x
       
if __name__ == "__main__":
    main()