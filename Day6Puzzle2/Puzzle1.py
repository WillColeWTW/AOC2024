from os.path import dirname

def get_guard_path_steps(space:list[list[str]]) -> int:
    
    height, width = len(space), len(space[0])
    squashed_space = [space[x][y] for x in range(0,height) for y in range(0,width)]
    direction_moves_dict = {1:-width, 2:1, 3:width, 4:-1}  # steps taken in 1-d, transposing N-E-S-W
    
    current_position, current_direction = [(i, {'^':1,'>':2,'v':3,'<':4}[squashed_space[i]]) for i in range(0, len(squashed_space)) if squashed_space[i] in ['^','>','v','<']][0]
    move = direction_moves_dict[current_direction]
    (can_continue) = True
    
    while((can_continue)):
        if((current_position + move) > 0 and (current_position + move) < len(squashed_space)):
            if(squashed_space[(current_position + move)] == '#'):
                move = direction_moves_dict[(current_direction + 1) % 4]
            else:
                current_position = current_position + move
                squashed_space[current_position + move] = 'X'
        else:
            can_continue = False
        
    return squashed_space.count('X')

def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day6Dataset.txt'
    space = []
    with open(data_file_path,'r') as file:
        for row in file:
            space.append(row.replace('\n','')[:])
            
    x = get_guard_path_steps(space)
    # print(x)
    return x
    
if __name__ == "__main__":
    main()