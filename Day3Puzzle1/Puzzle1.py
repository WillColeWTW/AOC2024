from os.path import dirname
import re

def sumproduct_all(memory:str) -> int:
    cleaned_memory = re.findall('[m][u][l]\\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\\)',memory)
    return sum([int(y)*int(z) for y, z in [x[4:len(x)-1].split(',') for x in cleaned_memory]])

def main():
    
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day3Dataset.txt'
    ridiculously_long_corrupted_memory_string = ""

    with open(data_file_path,'r') as file:
        for row in file:
            ridiculously_long_corrupted_memory_string += row
    x = sumproduct_all(ridiculously_long_corrupted_memory_string)
    # print(x)
    return x
    
if __name__ == "__main__":
    main()