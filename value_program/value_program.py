# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    rows = len(grid)
    cols = len(grid[0])
    marked = [[0] * cols for c in range(rows)]

    x = goal[0]
    y = goal[1]
    c = 0
    value = [[99] * cols for c in range(rows)]
    value[x][y] = c
    marked[x][y] = 1

    open_list = [[c, x, y]]
    while len(open_list) > 0:
        open_list.sort(reverse=True)
        check = open_list.pop()
        x = check[1]
        y = check[2]
        c = check[0]

        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < rows and y2 >= 0 and y2 < cols:
                if marked[x2][y2] == 0 and grid[x2][y2] == 0:
                    c2 = c + cost
                    marked[x2][y2] = 1
                    value[x2][y2] = c2

                    open_list.append([c2, x2, y2])

    return value


result = compute_value(grid, goal, cost)
for r in result:
    print(r)