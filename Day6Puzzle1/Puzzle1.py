from os.path import dirname

def get_guard_path_steps(space:list[list[str]]) -> int:

    height, width = len(space), len(space[0])
    squashed_space = [space[x][y] for x in range(0,height) for y in range(0,width)]
    direction_moves_dict = {0:-width, 1:1, 2:width, 3:-1}
    
    current_position, current_direction = [(i, {'^':0,'>':1,'v':2,'<':3}[squashed_space[i]]) for i in range(0, len(squashed_space)) if squashed_space[i] in ['^','>','v','<']][0]
    move = direction_moves_dict[current_direction]
    
    can_continue = True
    while can_continue:
        if((current_position + move) > 0 
            and (current_position + move) < len(squashed_space)
            and (   not((current_position + move) % width == 1 and move == 1) 
                 or not((current_position + move) % width == (width - 1) and move == -1))):
            if(squashed_space[(current_position + move)] == '#'):
                current_direction += 1
                move = direction_moves_dict[(current_direction) % 3]
            else:
                squashed_space[(current_position + move)] = 'X'
                current_position += move
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