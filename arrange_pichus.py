#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code in CSCI B551, Fall 2022.

import sys


# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Find pichu locations
def find_all_pichus(house_map):
    return [(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"]

# Validating the pichu locations on the map
def is_valid_successor(house_map):
    M = len(house_map)
    N = len(house_map[0])

    pichu_locations = find_all_pichus(house_map)
    
    for p_loc in pichu_locations:
        (row, col) = p_loc
        # Checking up along vettically
        for i in range(row-1, 0, -1):
            if house_map[i][col] in ['X','@']:
                break;
            elif house_map[i][col] == 'p':
                return False
        
        # Checking vertically down
        for i in range(row+1, M):
            if house_map[i][col] in ['X','@']:
                break;
            elif house_map[i][col] == 'p':
                return False

        # Checking left along the same x-axis
        for j in range(col-1, 0, -1):
            if house_map[row][j] in ['X','@']:
                break;
            elif house_map[row][j] == 'p':
                return False

        # Checking right horizontally
        for j in range(col+1, N):
            if house_map[row][j] in ['X','@']:
                break;
            elif house_map[row][j] == 'p':
                return False

        # Checking all  4 diagonals - NW, SE, NE, SW
        
        x,y = row,col
        while(x>0 and y>0):
            x-=1
            y-=1
            if house_map[x][y] in ['X','@']:
                break;
            elif house_map[x][y] == 'p':
                return False
        
        x,y = row,col
        while(x<M-1 and y<N-1):
            x+=1
            y+=1
            if house_map[x][y] in ['X','@']:
                break;
            elif house_map[x][y] == 'p':
                return False

        x,y = row,col
        while(x>0 and y<N-1):
            x-=1
            y+=1
            if house_map[x][y] in ['X','@']:
                break;
            elif house_map[x][y] == 'p':
                return False
        
        x,y = row,col
        while(x<M-1 and y>0):
            x+=1
            y-=1
            if house_map[x][y] in ['X','@']:
                break;
            elif house_map[x][y] == 'p':
                return False

    return True
    
    

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop(0) ):
            if is_valid_successor(new_house_map):
                if is_goal(new_house_map,k):
                    return(new_house_map,True)
                else:
                    fringe.append(new_house_map)
    else:
        return ('', False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


