
import random

# my global variables
obstacles = []

my_x = -97
my_y = 197


def does_it_overlap(obstacles, point):
    """
    This function checks if the obstacle we are trying to create overlaps
    with any of the obstacles already in the list.
    :Params - obstacles - (list of tuples) list of aleady existing obstacles
            - point - (tuple) the new obstacle we are trying to create
    :Return - return true if it overlaps, false if it doesnt
    """
    if obstacles == []:
        return False
    for obstacle in obstacles:   
        if point[0] >= obstacle[0] and point[0] <= obstacle[0]+4: 
            if point[1] >= obstacle[1] and point[1] <= obstacle[1]+4:
                return True
    return False


def create_rectangle_horizontals(vertical_wall, start_x, end_x):
    
    global obstacles

    my_door = random.randrange(start_x+4, end_x-8 ,4)

    for i in range(start_x, end_x, 4):
        if i == my_door or i == my_door+4:
            continue
        point = (i, vertical_wall)
        obstacles.append(point)


def create_rectangle_verticals(horizontal_wall, start_y, end_y):
    
    global obstacles

    my_door = random.randrange(start_y, end_y-8, 4)

    for i in range(start_y, end_y, 4):  
        if i == my_door or i == my_door+4:
            continue
        point = (horizontal_wall, i)
        obstacles.append(point)


def create_obstacles(min_x, min_y, max_x, max_y):
    """
    Function creates a list of obstacles. Calls the the create_obstacle function and 
    does_it_overlap function.
    :Return - (list of tuples) returns a list with all the obstacles in it as tuples.
    """
    global obstacles
    obstacles = []

    upper_wall = 186
    lower_wall = -190
    left_wall = -90
    right_wall = 86

    start_x = -90
    end_x = 90
    start_y = -186
    end_y = 186

    number_of_rectangles = 6
    
    for i in range(number_of_rectangles):
        create_rectangle_horizontals(upper_wall, start_x, end_x)
        create_rectangle_horizontals(lower_wall, start_x, end_x)
        create_rectangle_verticals(left_wall, start_y, end_y)
        create_rectangle_verticals(right_wall, start_y, end_y)
        
        upper_wall -= 14
        lower_wall += 14
        left_wall += 14
        right_wall -= 14

        start_x += 14
        end_x -= 14
        start_y += 14
        end_y -= 14 
     
    return obstacles


def get_obstacles():
         
    return obstacles
    
        

def is_position_blocked(x2, y2):
    """
    This function checks if the the position that the robot is trying to 
    land on blocked.
    :Params - x2 and xy are the coordinates of the new potential position of 
            the robot
    :Return - returns True if position overlaps and false if it doesnt
    """
    point = (x2,y2)
    if does_it_overlap(obstacles, point):
        return True
    return False

def is_path_blocked(x1,y1,x2,y2):
    """
    This function checks if the path that the robot is heading to blocked
    depending on where the new coordinates say the robot should go.
    :Params - x1 and y1 are the coordinates of the position of the robot. x2 and y2 are 
            the coordinates of the new position robot should go to.
    :Return - Returns true if there is an obstacle in the way and false if there isn't.
    """
    
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    blocked = False
    if x1 == x2:
        for i in range(min_y, max_y + 1):
            if is_position_blocked(x1, i) == True:
                blocked = True           
    elif y1 == y2:
        for i in range(min_x, max_x + 1):
            if is_position_blocked(i, y1) == True:
                blocked = True
    return blocked


def delete_list():
    obstacles = []
