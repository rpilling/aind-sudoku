assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# Notations & Definitions 

rows = 'ABCDEFGHI'
cols = '123456789'
digits = cols

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
dia1_units = [[a[0]+a[1] for a in zip(rows,cols)]]
dia2_units = [[a[0]+a[1] for a in zip(rows,cols[::-1])]]

unitlist = row_units + column_units + square_units + dia1_units + dia2_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    index = {}
    values = list(grid)
    for i in range(0,len(grid)):
        index[boxes[i]] = values[i]
        if index[boxes[i]] == '.':
            index[boxes[i]] = '123456789'
    return index

# Strategies

def eliminate(values):
    given_values = {}
    for box in values: # for entries in sudoku dictionary 
        if len(values[box]) == 1: # and entries which only have one value  
            given_values[box] = values[box] # create new dictionary for given_values
        for box in given_values: # for each entry (e.g. A3) in given_values
            for peer in peers[box]: # and each peer of the specific entry (e.g. A3)  
                values[peer] = values[peer].replace(values[box],'') # remove given_value from peer 
    return values 

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # find all boxes with two values
    
    pairs = [box for box in values.keys() if len(values[box]) == 2]
            
    for box in pairs: # find a way to split
        pair_value = values[box]
        for unit in units[box]:
            tplaces = [box for box in unit if values[box] == pair_value]
            if len(tplaces) == 2:
                not_tplace = [box for box in unit if box not in tplaces]
                for not_twin in not_tplace:
                    for digit in pair_value:
                        values[not_twin] = values[not_twin].replace(digit,'')
    return values


def only_choice(values):    # Finalize all values that are the only choice for a unit.
    for unit in unitlist:
        for digit in '123456789':
            dplaces = []
            for box in unit:
                if digit in values[box]:
                    dplaces.append(box)
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):  # Constraint propagation to combine eliminate and only_choice
    stalled = False
    while not stalled: 
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1]) # Check how many boxes have a determined value

        only_choice(eliminate(values)) 

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1]) # Check how many boxes have a determined value, to compare

        stalled = solved_values_before == solved_values_after

        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # (1) First, reduce the puzzle using the previous function

    values = reduce_puzzle(values) 

    if values is False:                            ## Failed earlier
        return False 
    
    if all(len(values[box]) == 1 for box in boxes):    ## Solved! 
        return values

    # (2) Choose one of the unfilled squares with the fewest possibilities

    n,box = min((len(values[box]),box) for box in boxes if len(values[box]) > 1)

    for value in values[box]:
        new_sudoku = values.copy()
        new_sudoku[box] = value
        attempt = search(new_sudoku)
        if attempt:
                return attempt

diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))
    

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(eliminate(grid_values(diag_sudoku_grid)))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
