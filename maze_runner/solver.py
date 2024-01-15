"""
Keep your right hand on the wall at all times. Keep track of how much you’ve turned in degrees. Every time you turn right, add 90 degrees and every time you turn left, subtract 90 degrees. For example:

 - if you turn right and then right again, then you’ve turned 180 degrees.
 - if you turn left and left again, then you’ve turned -180 degrees.
 - if you turn right, right, right, right, and then right, you’ve turned 450 degrees.
 - if you turn right and then left, you’ve turned 0 degrees.

If the number of degrees you’ve turned is 0, the direction you’re heading is the same one you started at, and you reach a place where you can either go straight or turn right, then take your hand off the wall and go straight. This helps you avoid getting stuck in some endless loops.
"""

import sys, time, import_helper
from maze import maze_load as maze_load
from world import worlds as world
robot = import_helper.dynamic_import("robot") # dynamic = stop importing loop
from import_helper import dynamic_import

wallhug = False
turned = 0
fake_wallhug = False
fake_turn = 0


def find_next_wall(robot_name, direction):
    """
    Checks the direciton we are going, and finding out if the position to the left is an obstacle or not, to be able to hug the wall. so once it leaves a wall, it turns left and forward to find out if there is a wall there, if there is continue against that wall. Else move back and check the right hand side if there is a wall
    :returns hugging the side which has a wall:
    """
    global turned, wallhug

    next_direction_blocked = False

    if direction == 0:
        next_direction_blocked = maze_load.is_position_blocked(world.position_x, world.position_y - 1)
    if direction == 1:
        next_direction_blocked = maze_load.is_position_blocked(world.position_x + 1, world.position_y)
    if direction == 2:
        next_direction_blocked = maze_load.is_position_blocked(world.position_x, world.position_y - 1)
    if direction == 3:
        next_direction_blocked =  maze_load.is_position_blocked(world.position_x - 1, world.position_y)

    robot.handle_command(robot_name, "left")
    robot.handle_command(robot_name, "forward 1")
    if next_direction_blocked:
        return
    else:
        robot.handle_command(robot_name, "back 1")
        robot.handle_command(robot_name, "right")
    robot.handle_command(robot_name, "right")
    turned -= 1
    robot.handle_command(robot_name, "forward 1")
    if next_direction_blocked:
        return


def end_location(direction):
    """
    checks where the end location shall be for the maze runner, as well as which wall we need to finish against.
    :returns wall side y(top/bottom) or x(left/right), and the position of the wall on that side:
    """
    if direction == "top":
        end_position = 200
        return "y", end_position 
    elif direction == "bottom":
        end_position = -200
        return "y", end_position 
    elif direction == "left":
        end_position = -100
        return "x", end_position 
    elif direction == "right":
        end_position = 100
        return "x", end_position 


def maze_checker(direction):
    """
    Checks the direction of the turtle, and then sets up the variables for the
    turtle to check against in the maze solver
    """

    path_block = False
    end_position = 0
    next_position_blocked = False

    if direction == 0: 
        path_block = maze_load.is_path_blocked(world.position_x, world.position_y, world.position_x, world.position_y + 1)
        end_position = 200
        next_position_blocked = maze_load.is_position_blocked(world.position_x + 1, world.position_y)
    if direction == 1:
        path_block = maze_load.is_path_blocked(world.position_x, world.position_y, world.position_x + 1, world.position_y)
        end_position = 100
        next_position_blocked = maze_load.is_position_blocked(world.position_x, world.position_y - 1)
    if direction == 2: 
        path_block = maze_load.is_path_blocked(world.position_x, world.position_y, world.position_x, world.position_y - 1)
        end_position = -200
        next_position_blocked = maze_load.is_position_blocked(world.position_x - 1, world.position_y)
    if direction == 3: 
        path_block = maze_load.is_path_blocked(world.position_x, world.position_y, world.position_x - 1, world.position_y)
        end_position = -100
        next_position_blocked = maze_load.is_position_blocked(world.position_x, world.position_y + 1)

    return path_block, end_position, next_position_blocked


def solving_the_maze(robot_name, direction, boundry):
    """
    This functions is run to solve the maze.
    1. It checks the results of the maze_checker functions, to set up some vars 
    Checks if the path is blocked and goes accordingly:
    2. If path is blocked it checks if you are on the boundry and path is 
    blocked, if so will set up some fake wallhug modes. 
    3. then turns left, else if step 2 is false it just turns left,
    If path is not blocked, it does the following:
    4. checks if on the boundry and if you are on the end position. then sets up some fake values while you are boundry hugging
    5. If you are in wallhugging, the position on side is blocked, move forward.
    6. If you are at end of a wall run find_next_wall, to continue wallhugging
    7. Else just move forward
    """

    global turned, wallhug, fake_wallhug, fake_turn

    path_block, end_position, next_position_blocked = maze_checker(world.current_direction_index)

    if path_block:
        if boundry == True and path_block == True:
            wallhug = fake_wallhug
            turned = fake_turn
        robot.handle_command(robot_name, "left")
        turned += 1
    else:
        if boundry == True and (world.position_y if direction == 0 or direction == 2 else world.position_x) == end_position:
            robot.handle_command(robot_name, "left")
            fake_turn = turned + 1
            turned = 0
            fake_wallhug = wallhug
            wallhug = False
        elif wallhug == True:
            if next_position_blocked:
                robot.handle_command(robot_name, "forward 1")
            else:
                find_next_wall(robot_name, world.current_direction_index)
        else:
            robot.handle_command(robot_name, "forward 1")


def maze_solver(robot_name, direction):
    """
    1. checks which direction was passed, if it was empty default top, else run through end location to find out which values (end_wall ?x/y?), (end_position ?(-)200/(-)100?).
    2. uses ternary to check which wall and which co-ordinate you must run towards
    3. checks howmany times you have turned vs if you are in wallhugger mode
    4. calls the solving algo based on the direction you are currently facing
    5. checks if you are on the boundary or not
    6. (bonus checks howlong it took to solve time())
    :return True when you are at the end, and which direction you are on:
    """
    global turned, wallhug

    print(f"> {robot_name} starting maze run..")
    starttime = time.time()
    # world.turtle.tracer(0)

    if direction == '':
        direction = "top"

    (end_wall, end_position) = end_location(direction)

    boundry = False

    while (world.position_y if end_wall == "y" else world.position_x) != end_position:
        if turned != 0:
            wallhug = True
        if turned == 0:
            wallhug = False
        
        if world.current_direction_index == 0:
            solving_the_maze(robot_name, world.current_direction_index, boundry)
        if world.current_direction_index == 1:
            solving_the_maze(robot_name, world.current_direction_index, boundry)
        if world.current_direction_index == 2:
            solving_the_maze(robot_name, world.current_direction_index, boundry)
        if world.current_direction_index == 3:
            solving_the_maze(robot_name, world.current_direction_index, boundry)

        if world.position_y == 200 or world.position_y == -200 or world.position_x == -100 or world.position_x == 100:
            boundry = True
        else:
            boundry = False

    print(f"time was: {time.time()- starttime}")
    return True, robot_name+": I am at the "+direction+" edge."