# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):
    rows = len(grid)
    cols = len(grid[0])

    x = goal[0]
    y = goal[1]
    c = 0
    values = [[[999] * cols for c in range(rows)]] * 3
    policy2D = [[' '] * cols for c in range(rows)]
    marked = [[[0] * cols for c in range(rows)]] * 3
    action = [[[0] * cols for c in range(rows)]] * 3

    marked[x][y][0] = 1
    marked[x][y][1] = 1
    marked[x][y][2] = 1
    values[x][y][0] = c
    values[x][y][1] = c
    values[x][y][2] = c

    open_list = []
    open_list.append([] * 3)
    open_list[0].append([[c, x, y]])
    open_list[1].append([[c, x, y]])
    open_list[2].append([[c, x, y]])
    for d in range(3):
        while len(open_list[d]) > 0:
            open_list[d].sort(reverse=True)
            check = open_list[d].pop()
            x = check[1]
            y = check[2]
            c = check[0]

            for i in range(len(forward)):
                x2 = x + forward[i][0]
                y2 = y + forward[i][1]
                if x2 >= 0 and x2 < rows and y2 >= 0 and y2 < cols:
                    if marked[x2][y2][d] == 0 and grid[x2][y2] == 0:
                        c2 = c + cost[d]
                        marked[x2][y2][d] = 1
                        values[x2][y2][d] = c2

                        open_list[d].append([c2, x2, y2])

    return policy2D, values

result, values = optimum_policy2D(grid, init, goal, cost)
for d in range(3):
    print("---------------------")
    for v in values[d]:
        print(v)

    print("---------------------")
    print()