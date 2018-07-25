# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------

import grader
from test import delta, delta_name

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def collect_adjacent(grid, v, marked, rows, cols):
    adjacent = []
    # Try UP, LEFT, DOWN and RIGHT direction
    for i in range(len(delta)):
        next_x = v[0] + delta[i][0]
        next_y = v[1] + delta[i][1]
        if next_x >= 0 and next_y >= 0 and \
                next_x < rows and next_y < cols and \
                grid[next_x][next_y] != 1 and \
                marked[next_x][next_y] == -1:
            adjacent.append([next_x, next_y])

    return adjacent


def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    rows = len(grid)
    cols = len(grid[0])
    marked = [[-1] * cols for c in range(rows)]
    marked[init[0]][init[1]] = 0
    distTo = [[0] * cols for c in range(rows)]
    open_list = []
    step = 1

    open_list.append([0, init[0], init[1]])

    while len(open_list) > 0:
        check = open_list.pop()

        p = [check[1], check[2]]
        if check[1] == goal[0] and check[2] == goal[1]:
            return check

        adjacent = collect_adjacent(grid, p, marked, rows, cols)

        for adj in adjacent:
            distance = distTo[p[0]][p[1]] + cost
            distTo[adj[0]][adj[1]] = distance
            marked[adj[0]][adj[1]] = step
            step += 1
            open_list.append([distance, adj[0], adj[1]])

        open_list.sort(reverse=True)

    expand = marked
    return expand

try:
    response = grader.run_grader(search)
    print(response)

except Exception as err:
    print(str(err))