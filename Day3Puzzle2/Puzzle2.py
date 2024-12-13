from os.path import dirname
import re

def sumproduct_conditional_do_multiplications(memory:str) -> int:
    runs = memory.split('do()')
    total = 0
    for run in runs:
        run_memory = run.split("don't()")[0]
        run_memory_multiplications = re.findall('[m][u][l]\\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\\)',run_memory)
        total += sum([int(y)*int(z) for y, z in [x[4:len(x)-1].split(',') for x in run_memory_multiplications]])
    return total

def main():
    
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day3Dataset.txt'
    ridiculously_long_corrupted_memory_string = ""

    with open(data_file_path,'r') as file:
        for row in file:
            ridiculously_long_corrupted_memory_string += row
    x = sumproduct_conditional_do_multiplications(ridiculously_long_corrupted_memory_string)
    # print(x)
    return x
    
if __name__ == "__main__":
    main()