import random

obstacles = []

def create_obstacles(min_x, min_y, max_x, max_y):
    """
    gets the obstacles global, and for each instance in a randomly generated
    number between 1 and 10 it will generate a random position between x: -196 to 196. and for y: -96 to 96 (so the squares dont go out of bounds)
    :returns the list of obstacles"
    """
    global obstacles 

    obstacles = []

    for i in range(random.randint(1, 10)):
        x = random.randint(min_x + 4, max_x - 4)
        y = random.randint(min_y + 4, max_y - 4)
        obstacles.append((x,y))
    return obstacles


def is_position_blocked(x,y):
    """
    foreach set of tuples inside of the obstacles lists, it checks if the position of either x or y (which is the robot passed position) is in the range of the obstacle, 
    :returns True if the position is blocked:
    :returns False if the position is not blocked:
    """
    for tups in obstacles:
        tup_x = tups[0]
        tup_y = tups[1]
        if (tup_x <= x <= (tup_x + 4)) and (tup_y <= y <= (tup_y + 4)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    takes the min and max values passed through with x1 and y1 being the co-ords
    that you are at and x2 and y2 the co-ords that you are moving to. and checks
    that if the position you are moving towards has an obstacle in the way
    :returns True if the path is blocked:
    :returns False if the path is not blocked:
    """

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if is_position_blocked(x1, i) :
                # print(x1, i)
                return True
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if is_position_blocked(i, y1):
                return True
    return False


def get_obstacles():
    """Returns obstacles lists"""
    return obstacles