import random

# empty obstacles global to be initialised later
obstacles = []
# number of squares within the boundry
# increase number to increase difficulty
squares = 10
# width of the holes
hole_width = 5

def create_horizontal(min, max, y, draw_side, hole_side):
    """Creates horizontal line between two points.
    | Hole is created on the specified hole line."""

    global obstacles

    hole = None
    if draw_side == hole_side:        
        hole = random.randint(min+hole_width, max-hole_width)

    for pos in range(min, max+1, 4):
        if not (draw_side == hole_side and hole-hole_width <= pos <= hole+hole_width) :
            obstacles.append((pos,y))

def create_vertical(min, max, x, draw_side, hole_side):
    """Creates verticle line between two points.
    | Hole is created on the specified hole line."""

    global obstacles

    hole = None
    if draw_side == hole_side:        
        hole = random.randint(min+hole_width, max-hole_width)

    for pos in range(min, max+1, 4):
        if not (draw_side == hole_side and hole-hole_width <= pos <= hole+hole_width) :
            obstacles.append((x, pos))


def create_blockage(min_x, min_y, max_x, max_y, square_i):
    """Creates blockage at a random point from square to next square.
    | Selects random side.
    | Creates from random point, outwards from square of length equal to length."""

    block_side = random.choice(["left", "right", "bottom", "top"])
    if block_side == "left":
        create_horizontal(min_x - int(max_x/square_i),min_x, random.randint(min_y, max_y), "block", None)

    elif block_side == "right":
        create_horizontal(max_x,max_x + int(max_x/square_i), random.randint(min_y, max_y), "block", None)

    elif block_side == "bottom":
        create_vertical(min_y - int(max_y/square_i),min_y, random.randint(min_x, max_x), "block", None)

    elif block_side == "top":
        create_vertical(max_y, max_y + int(max_y/square_i), random.randint(min_x, max_x), "block", None)

def create_square(min_x, min_y, max_x, max_y):
    """Generates square based on co-ordinates.
    | Chooses a side for the hole.
    | Creates line based on side."""

    hole_side = random.choice(["left", "right", "bottom", "top"])

    create_vertical(min_y, max_y, min_x, "left", hole_side)
    create_horizontal(min_x, max_x, max_y, "top", hole_side)
    create_horizontal(min_x, max_x, min_y, "bottom", hole_side)
    create_vertical(min_y, max_y, max_x, "right", hole_side)


def create_maze(min_x, min_y, max_x, max_y):
    """Generates maze based on how many squares are desired inside.
    | Loop through range of desired squares.
    | Pass co-ordinates of new square into create_square.
    | Pass co-ordinates of new square into create_blockage, as well as the index."""

    for i in range(squares-1, 0, -1):
        create_square(int(min_x*i/squares), int(min_y*i/squares), int(max_x*i/squares), int(max_y*i/squares))
        if i < squares:
            create_blockage(int(min_x*i/squares), int(min_y*i/squares), int(max_x*i/squares), int(max_y*i/squares), i)


def create_obstacles(min_x, min_y, max_x, max_y):
    """Generates obstacles by making random co-odinates up to 10 times."""

    global obstacles
    obstacles = []

    create_maze(min_x-2, min_y-2, max_x-2, max_y-2)

    return obstacles


def is_position_blocked(x,y):
    """Checks if current co-ordinate falls in obstacle."""

    for i in obstacles:
        if i[0] <= x <= i[0] + 4:
            if i[1] <= y <= i[1] + 4:
                return True


def check_path(start, end, same, axis):
    """Function checks if path is blocked based on 2 co-ordinates
    | Loops through co-ordinates changes from start to end position.
    | Checks which axis move was made.
    """

    for i in range(start, end + 1):
        if axis == "x":
            if is_position_blocked(i, same):
                return True
        else:
            if is_position_blocked(same, i):
                return True


def is_path_blocked(x1, y1, x2, y2): 
    """Function checks if path is blocked by calling appropriate functions
    | Checks if move was on x/y axis, and if move was backward or forward.
    | Calls check_path with co-ordinates.
    """

    if x2 > x1:
        return check_path(x1, x2, y1, "x")
    elif x1 > x2:
        return check_path(x2, x1, y1, "x")
    elif y2 > y1:
        return check_path(y1, y2, x1, "y")
    else:
        return check_path(y2, y1, x1, "y")

def get_obstacles():
    return obstacles
