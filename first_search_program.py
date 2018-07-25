# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def collect_adjacent(v, marked):
    adjacent = []
    # Try UP, LEFT, DOWN and RIGHT direction
    for i in range(len(delta)):
        next_x = v[0] + delta[i][0]
        next_y = v[1] + delta[i][1]
        if next_x >= 0 and next_y >= 0:
            if grid[next_x][next_y] != 1:
                if marked[next_x][next_y] == False:
                    adjacent.append([next_x, next_y])

    return adjacent


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    rows = len(grid)
    cols = len(grid[0])
    marked = [[False] * cols for c in range(rows)]
    marked[init[0]][init[1]] = True
    distTo = [[0] * cols for c in range(rows)]
    path = []

    adjacent = collect_adjacent(init, marked)
    p = init
    while len(adjacent) > 0:
        adj = adjacent[-1]
        distTo[adj[0]][adj[1]] = distTo[p[0]][p[1]] + cost
    while len(adjacent) > 0:
        adj = adjacent.pop()
        distTo[adj[0]][adj[1]] = distTo[p[0]][p[1]] + cost
        marked[adj[0]][adj[1]] = True
        n = collect_adjacent(adj, marked)
        if len(n) > 0:
            p = adj
            while len(n) > 0:
                adjacent.append(n.pop())

    return path


path = search(grid, init, goal, cost)