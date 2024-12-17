from os.path import dirname
from checklist import repiece

def get_guard_time_loops(space:list[list[str]]) -> int:

    height, width = len(space), len(space[0])
    squashed_space = [space[x][y] for x in range(0,height) for y in range(0,width)]
    direction_moves_dict = {0:-width, 1:1, 2:width, 3:-1}
    direction_symbols = {0:'^',1:'>',2:'v',3:'<'}
    
    current_position, current_direction = [(i, {'^':0,'>':1,'v':2,'<':3}[squashed_space[i]]) for i in range(0, len(squashed_space)) if squashed_space[i] in ['^','>','v','<']][0]
    move = direction_moves_dict[current_direction]
    loops = 0
    can_continue = True
    squashed_space[current_position] = 'X'
    
    while can_continue:
        # constaints on grid
        if((current_position + move) > 0 
            and (current_position + move) < len(squashed_space)
            and (   not((current_position + move) % width == 1 and move == 1) 
                 or not((current_position + move) % width == (width - 1) and move == -1))):
            
        # conditions for adding a loop
            if(squashed_space[current_position + direction_moves_dict[(current_direction+1) % 4]] == direction_symbols[(current_direction+1) % 4]): 
                repiece(squashed_space, width, height , dirname(__file__) + '\\Day6DatasetOutput.txt')
                loops += 1
                
            if(squashed_space[current_position + direction_moves_dict[(current_direction+1) % 4]] == direction_symbols[(current_direction+2) % 4]
                and squashed_space[current_position + move*2] == '#'): 
                repiece(squashed_space, width, height , dirname(__file__) + '\\Day6DatasetOutput.txt')
                loops += 1
        
        # change direction
            if(squashed_space[(current_position + move)] == '#'):
                current_direction += 1
                move = direction_moves_dict[(current_direction) % 4]

            squashed_space[(current_position + move)] = direction_symbols[current_direction % 4]
            current_position += move
        else:
            can_continue = False
    
    return loops #squashed_space.count('X')

def main():
    current_path = dirname(__file__)
    data_file_path = current_path + '\\Day6DatasetSample.txt'
    
    space = []
    with open(data_file_path,'r') as file:
        for row in file:
            space.append(row.replace('\n','')[:])
    
    x = get_guard_time_loops(space)
    print(x)
    return x
    
if __name__ == "__main__":
    main()