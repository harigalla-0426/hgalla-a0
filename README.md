# hgalla-a0

### Part -1: Pichu Navigation

- For part-1, I have used the used most of the helper functions as is, and changed the code only in the search method. Though additionally, I have added a helper function which will return an updated path for me based on the move.
- The search algorithm used here is BFS (Breadth First Search), which essentially is a complete solution.
- However, the existing solution when run, gets stuck in an infinite loop as it keeps adding possible states into the fringe without keeping track of the visited ones and popping them accordingly.
- For my solution, instead of just keeping track of the visited states; I have used **Best-First Search** with **heuristic function**, which explores the most "**Promising**" State first.
- **f(s) = h(s); where h is the MANHATTAN DISTANCE (|x1-x2| + |y1-y2|)** between two points (x1,y1) (x2,y2)

1. Initial State: The maps given in MxN format with agent 'p' placed along with walls (X) and the target (@)
2. Cost Function: Each move costs 1 unit as the agent can move only up, down, left and right but not diagnally.
3. Successor Function: This encompasses the path the agent can move: UP, DOWN, LEFT, RIGHT
4. Valid States: The possible coordinates the agent can navigate to; which a) Lies in the boundaries of the matrix and b) is not blocked by a wall, i.e it is either '.' or '@'.
5. Goal State: A Valid state where the agent 'p' is able to navigate to the target **'@'**

### Part -2: Arranging Pichus

- For part-2, again I have modified the code in the solve method, but added a function called **is_valid_successor** to validate the successor house map.
- The search algorithm used here is BFS (Breadth First Search) and I have employed the same principle strategy of a general TREE-SEARCH, however without keeping track of the visited nodes, for backtracking purposes. All the valid states will be present in the fringe and considered until the fringe is finally empty.
- The existing solution just calculates the possible successors, while ignoring how the agents are placed in the map. This results in an invalid solution, where agents can see each other.
- The helper function **is_valid_successor** does the job of taking a valid housemap and validating it to ensure none of the agents are attacking each other. For this I have taken each agent into consideration and checked whether any other agent is in the line-of-sight for all eight directions: N,S,E,W,NE,NW,SE,SW (including diagnals)

1. Initial State: The maps given in MxN format with a single agent 'p' placed along with walls (X) and target(@)
2. Cost Function: Again this is 1 unit, as the agents are placed level-by-level starting from i=0.
3. Successor Function: This encompasses any housemap with the next agent placed in the available space '.'
4. Valid States: A house map with agents placed such that none can see each other
5. Goal State: A house map with k agents placed such that none can see each other
