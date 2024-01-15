obstacles = []

def create_obstacles(min_x, min_y, max_x, max_y):
    """Create a random number of obscatles up to 10 inside the valid coords

    :param min_y: Minimum valid Y value
    :param min_x: Minimum valid x value
    :param max_y: Maximum valid Y value
    :param max_x: Maximum valid X value
    """
    global obstacles 
    obstacles = []
    draw_obstacle_line(-70,120, 70, 120)
    draw_obstacle_line(-70, -120, -70, 120)
    draw_obstacle_line(70, -120, 70, 125)
    draw_obstacle_line(-50 ,-100,-50, 100)
    draw_obstacle_line(-50, 100, 50, 100) 
    draw_obstacle_line(50 ,-120, 50, 105)   
    draw_obstacle_line(-70, -120, 50, -120)
    draw_obstacle_line(66, -120, 100, -120)
    draw_obstacle_line(0, 140, 0, 180)
    draw_obstacle_line(-30, -100, 50, -100)
    draw_obstacle_line(-50, -30, 30, -30)
    draw_obstacle_line(-30, -80, -30, -25)
    draw_obstacle_line(30, -30, 30, 80)
    draw_obstacle_line(-50, 80, 10, 80)
    draw_obstacle_line(50, -200, 50, -150)
    draw_obstacle_line(-70, -180, -70, -120)
    draw_obstacle_line(-70, -180, 30, -180)
    draw_obstacle_line(-50, -150, 55, -150)
    draw_obstacle_line(-30, 30, 30, 30)
    draw_obstacle_line(10, -100, 10, -50)
    draw_obstacle_line(-100, 140, -20, 140)
    draw_obstacle_line(-4, 140, 100, 140)
    draw_obstacle_line(-80, 180, 5, 180)
    draw_obstacle_line(70, 170, 70, 200)
    draw_obstacle_line(40, 140, 40, 170)
    return obstacles


def draw_obstacle_line(start_x, start_y, end_x, end_y):
    global obstacles
    if start_x == end_x:
        for y_coord in range(start_y, end_y, 5):
            obstacles.append((start_x, y_coord))
    if start_y == end_y:
        for x_coord in range(start_x, end_x, 5):
            obstacles.append((x_coord, start_y))


def is_position_blocked(x, y):
    """Is the given position blocked by an obsticle

    :param x: X coord to check
    :param y: Y coord to check
    :return:  returns a bool based on whether the coord is blokcked of not
    """
    is_blocked = False
    for obstacle in obstacles:
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
    for obstacle in obstacles:
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
    des_obs = is_position_blocked(x2, y2)
    return is_blocked or des_obs
def get_obstacles():
    """Returns the obstacles
    """
    return obstacles