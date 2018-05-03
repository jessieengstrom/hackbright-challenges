def find_center(matrix):
    """Find the center of the matrix."""

    # if the number of columns is even pick the bigger middle column
    if len(matrix[0]) % 2 == 0:
        if len(matrix[0]) / 2 > len(matrix[0]) / 2 - 1:
            middle_col = len(matrix[0]) / 2
        else:
            middle_col = len(matrix[0]) / 2 - 1
    else:
        middle_col = len(matrix[0]) / 2

    # if the number of rows is even choose the bigger middle row
    if len(matrix) % 2 == 0:
        if matrix[len(matrix)/2][middle_col] > matrix[len(matrix)/2-1][middle_col]:
            middle_row = len(matrix) / 2
        else:
            middle_row = len(matrix) / 2 - 1
    else:
        middle_row = len(matrix) / 2

    # return the indexes (coordinates) and the value for the center of the matrix example: (7, (1, 2))
    return matrix[middle_row][middle_col], (middle_row, middle_col)


def find_largest(up, down, left, right, matrix):
    """Find the largest number surrounding the center."""

    # use the indexes to get the number that resides at the index above, below, right, and left of the rabbit
    if up:
        up_num = matrix[up[0]][up[1]]
    else:
        up_num = -1
    if down:
        down_num = matrix[down[0]][down[1]]
    else:
        down_num = -1
    if right:
        right_num = matrix[right[0]][right[1]]
    else:
        right_num = -1
    if left:
        left_num = matrix[left[0]][left[1]]
    else:
        left_num = -1

    # create a dictionary with the number as the key and the indexes as the values
    largest = {
        up_num: up,
        down_num: down,
        right_num: right,
        left_num: left
    }

    # get a list of all the keys
    largest_key = max(largest.keys())

    # return the largest key and its index example: (8 , (0, 2)) this is where the rabbit will move next
    return largest_key, largest[largest_key]


def get_up(row):
    """Get the index above rabbit."""
    return row - 1


def get_down(row):
    """Get the index below rabbit."""
    return row + 1


def get_left(col):
    """Get the index to the left of rabbit."""
    return col - 1


def get_right(col):
    """Get the index to the right of rabbit."""
    return col + 1


def move_rabbit(matrix):
    """Move rabbit and calculate carrots eaten."""

    # if the matrix is 1X1 return single value
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # find the indexes of the center of the matrix
    center = find_center(matrix)

    # declare carrots eaten variable
    carrots_eaten = 0

    up = 1
    down = 1
    left = 1
    right = 1

    # while the rabbit has carrots surrounding it
    while up != 0 or down != 0 or right != 0 or left != 0:

        center_coord = center[1]

        # eat carrots at the new position
        carrots_eaten += center[0]
        matrix[center_coord[0]][center_coord[1]] = 0

        # if row is not 0 then get the indexes (coordinates) for the row above the rabbit
        if center_coord[0] != 0:
            up = get_up(center_coord[0]), center_coord[1]
            if matrix[up[0]][up[1]] == 0:
                up = 0
        else:
            up = 0

        # if column is is not 0 then get the indexes (coordinates) for the column to the left of the rabbit
        if center_coord[1] != 0:
            left = center_coord[0], get_left(center_coord[1])
            if matrix[left[0]][left[1]] == 0:
                left = 0
        else:
            left = 0

        # if the column is not the last column then get the indexes (coordinates) for the column to the right of the rabbit
        if center_coord[1] != len(matrix[0]) - 1:
            right = center_coord[0], get_right(center_coord[1])
            if matrix[right[0]][right[1]] == 0:
                right = 0
        else:
            right = 0

        # if the row is not the last row then get the indexes (coordinates) for the row below the rabbit
        if center_coord[0] + 1 != len(matrix):
            down = get_down(center_coord[0]), center_coord[1]
            if matrix[down[0]][down[1]] == 0:
                down = 0
        else:
            down = 0

        # eat the carrots at the current position
        matrix[center_coord[0]][center_coord[1]] = 0

        # move rabbit to the position with the most carrots
        center = find_largest(up, down, left, right, matrix)

    return carrots_eaten

print move_rabbit([
    [5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8]
])

print move_rabbit([[7]])

print move_rabbit([[5, 7, 8, 6, 3]])

print move_rabbit([
    [5, 7, 8],
    [0, 0, 2]
])

print move_rabbit([
    [1, 0, 3, 0],
    [4, 5, 6, 7],
    [7, 0, 9, 0],
    [10, 0, 0, 0]
])

print move_rabbit([
    [1, 2],
    [0, 3],
    [4, 0]
])

print move_rabbit([[3, 7, 8, 6]])

print move_rabbit([[2, 1]])
