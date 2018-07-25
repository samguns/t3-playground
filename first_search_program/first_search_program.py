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
import grader
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

def collect_adjacent(grid, v, marked, rows, cols):
    adjacent = []
    # Try UP, LEFT, DOWN and RIGHT direction
    for i in range(len(delta)):
        next_x = v[0] + delta[i][0]
        next_y = v[1] + delta[i][1]
        if next_x >= 0 and next_y >= 0 and \
                next_x < rows and next_y < cols and \
                grid[next_x][next_y] != 1 and \
                marked[next_x][next_y] == False:
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
    open_list = []

    open_list.append([0, init[0], init[1]])

    while len(open_list) > 0:
        check = open_list.pop()
        # print("Take list item")
        # print(check)
        p = [check[1], check[2]]
        if check[1] == goal[0] and check[2] == goal[1]:
            return check

        adjacent = collect_adjacent(grid, p, marked, rows, cols)
        # print("New open list")

        for adj in adjacent:
            distance = distTo[p[0]][p[1]] + cost
            distTo[adj[0]][adj[1]] = distance
            marked[adj[0]][adj[1]] = True
            open_list.append([distance, adj[0], adj[1]])

        # print(open_list)
        # print("---------------")
        open_list.sort(reverse=True)

    return "fail"


try:
    response = grader.run_grader(search)
    print(response)

except Exception as err:
    print(str(err))