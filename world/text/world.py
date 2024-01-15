from maze import maze_load as obs

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def show_obstacles():
    """
    Creates the obstacles from create obs,
    checks if it exists and if it does prints out each position of the obstacles
    """
    obstacles = obs.create_obstacles(min_x, min_y, max_x, max_y)
    if obstacles:
        print("There are some obstacles:")
        for i in obs.get_obstacles():
            print(f"- At position {i[0]},{i[1]} (to {i[0] + 4},{i[1] + 4})")


def show_position(robot_name):
    """
    Shows the position of the robot after movement
    :returns: print statement of the positon
    """
    
    return print(f" > {robot_name} now at position ({str(position_x)},{position_y}).")


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    returns "blocked" if the path is blocked by an obstacle
    returns "allowed if the path is allowed and not out of bounds or obstacles
    else it returns range
    """
    global position_x, position_y

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    
    if obs.is_path_blocked(position_x, position_y, new_x, new_y):
        return "blocked"

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return "allowed"
    return "outbounds"


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    checked_pos = update_position(steps)

    if checked_pos == "allowed":
        return True, f" > {robot_name} moved forward by {str(steps)} steps."
    elif checked_pos == "blocked":
        return True, "Sorry, there is an obstacle in the way."
    else:
        return True, f"{robot_name}: Sorry, I cannot go outside my safe zone."


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    checked_pos = update_position(-steps)

    if checked_pos == "allowed":
        return True, f" > {robot_name} moved back by {str(steps)} steps."
    elif checked_pos == "blocked":
        return True, "Sorry, there is an obstacle in the way."
    else:
        return True, f"{robot_name}: Sorry, I cannot go outside my safe zone."


def turn_right(robot_name):
    """
    Do a 90 degree turn to the right, resets at 3
    :return: (True, right turn output text)
    """

    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, f" > {robot_name} turned right."


def turn_left(robot_name):
    """
    Do a 90 degree turn to the left, resets at 0
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, f" > {robot_name} turned left."


def sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return sprint(robot_name, steps - 1)