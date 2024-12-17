from os.path import dirname

def check_that_equation_possible(results: list[int], input_lists:list[list[int]]) -> int:
    # aim: recursively return the greatest result subject to the target result constraint
    def test_operators(target_result: int, run_result: int, inputs: list[int]) -> int:
        if run_result > target_result:
            return 0
        if len(inputs) == 0: 
            return run_result
        return max(test_operators(target_result, run_result*inputs[0], inputs[1:]),
                   test_operators(target_result, run_result+inputs[0], inputs[1:]),
                   test_operators(target_result, int('%d%d' % (run_result,inputs[0])), inputs[1:]))

    true_equations_sum = 0
    for i in range(len(input_lists)):
        if(test_operators(results[i], 0, input_lists[i]) == results[i]):
            true_equations_sum += results[i]

    return true_equations_sum

def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day7Dataset.txt'
    
    targets,  input_lists = [], []
    with open(data_file_path,'r') as file:
        for row in file:
            targets.append(int(row.split(':')[0]))
            input_lists.append(list(map(int, [i for i in row.split(':')[1].strip().replace('\n','').split(" ")])))
    
    x = check_that_equation_possible(targets, input_lists)
    #print(x)
    return x
    
if __name__ == "__main__":
    main()