#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [PUT YOUR NAME AND USERNAME HERE]
#
# Based on skeleton code provided in CSCI B551, Fall 2022.

import sys

# Parse the map from a given filename


def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Check if a row,col index pair is on the map


def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m

# Find the possible moves from position (row, col)


def moves(map, row, col):
    moves = ((row+1, col), (row-1, col), (row, col-1), (row, col+1))

    # Return only moves that are within the house_map and legal (i.e. go through open space ".")
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)


def search(house_map):
    # Find pichu start and target positions
    pichu_loc = target_loc = 0
    for i in range(len(house_map)):
        for j in range(len(house_map[0])):
            if house_map[i][j] == "p":
                pichu_loc = (i, j)
            elif house_map[i][j] == "@":
                target_loc = (i, j)

    print('locations', pichu_loc, target_loc)

    # initialize fringe and visited
    fringe = [(pichu_loc, '', 0)]
    visited = []

    while fringe:
        (curr_move, path, distance_to_goal) = fringe.pop()
        visited.append(curr_move)

        for move in moves(house_map, *curr_move):
            # Compute updated next path
            updated_path = return_updated_path(path, curr_move, move)

            if house_map[move[0]][move[1]] == "@":
                return (len(updated_path), updated_path)
            else:
                # Computing the manhattan distance - |x1-x2| + |y1-y2|
                distance_to_goal = abs(move[0] - target_loc[0])
                + abs(move[1] - target_loc[1])
                if move not in visited:
                    fringe.append((move, updated_path, len(updated_path) + distance_to_goal))

        # Sort the fringe according to the distances to pop the node with shortest distance first
        fringe.sort(key=lambda node: node[2], reverse=True)
    else:
        # No solution
        return (-1, '')


def return_updated_path(path, curr_move, move):
    x_diff = curr_move[0] - move[0]
    y_diff = curr_move[1] - move[1]
    if (x_diff == 0):
        if y_diff > 0:
            path += 'L'
        else:
            path += 'R'
    else:
        if x_diff > 0:
            path += 'U'
        else:
            path += 'D'
    return path


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + solution[1])
