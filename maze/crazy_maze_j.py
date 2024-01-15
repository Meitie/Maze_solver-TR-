import random
# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# creating the obstacles lists
obstacle_list = []

def obst():
    """Create a random number of obscatles up to 10 inside the valid coords

    :param min_y: Minimum valid Y value
    :param min_x: Minimum valid x value
    :param max_y: Maximum valid Y value
    :param max_x: Maximum valid X value
    """
    global obstacle_list 
    obstacle_list = []
    # num_of_obstacles = random.randint(0, 10)
    # for _ in range(num_of_obstacles):
    #     obstacle = (random.randint(min_x, max_x), random.randint(min_y, max_y))
    #     obstacle_list.append(obstacle)
    draw_obstacle_line(-70,120, 70, 120)
    draw_obstacle_line(-70, -120, -70, 120)
    draw_obstacle_line(70, -120, 70, 125)
    draw_obstacle_line(-50 ,-100,-50, 100)
    draw_obstacle_line(-50, 100, 50, 100) 
    draw_obstacle_line(50 ,-120, 50, 105)   
    draw_obstacle_line(-70, -120, 50, -120)
    draw_obstacle_line(70, -120, 100, -120)
    draw_obstacle_line(0, 140, 0, 200)
    return obstacle_list

def draw_obstacle_line(start_x, start_y, end_x, end_y):
    global obstacle_list
    if start_x == end_x:
        for y_coord in range(start_y, end_y, 5):
            obstacle_list.append((start_x, y_coord))
    if start_y == end_y:
        for x_coord in range(start_x, end_x, 5):
            obstacle_list.append((x_coord, start_y))


def is_position_blocked(x, y):
    """Is the given position blocked by an obsticle

    :param x: X coord to check
    :param y: Y coord to check
    :return:  returns a bool based on whether the coord is blokcked of not
    """
    is_blocked = False
    for obstacle in obstacle_list:
        if x >= obstacle[0] and x <= obstacle[0]+4:
            if y >= obstacle[1] and y <= obstacle[1]+4:
                is_blocked = True
    return(is_blocked)


def is_path_blocked(x1, y1, x2, y2):
    """Is the path between 2 coordinates blocked by an obstacle

    :param x1: The x coordinate of the start point
    :param y1: The y coordinate of the start point  
    :param x2: The x coordinate of the end point
    :param y2: The y coordinate of the end point
    :return: Returns a True based on whether the path between the the 2 given coords are blocked
    """
    is_blocked = False
    for obstacle in obstacle_list:
        # x is fixed
        if x1 == x2:
            #In the same x column as obstacle
            if x1 >= obstacle[0] and x1 <= obstacle[0]+4:
                if y1 < obstacle[1] and y2 >= obstacle[1]:
                    is_blocked = True
                    break
                elif y1 > obstacle[1] and y2 <= obstacle[1]:
                    is_blocked = True
                    break
        # y is fixed
        if y1 == y2:
            #In the same y row as obstacle
            if y1 >= obstacle[1] and y1 <= obstacle[1]+4:
                if x1 < obstacle[0] and  x2 >= obstacle[0]:
                    is_blocked = True
                    break
                elif x1 > obstacle[0] and x2 <= obstacle[0]:
                    is_blocked = True
                    break
    return(is_blocked)  


def get_obstacles():
    """Returns the obstacle_list
    """
    return obstacle_list