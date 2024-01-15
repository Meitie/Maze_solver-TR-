import random
import sys

obstacles = []

def get_obstacles():
    """
    returns obstacles haha
    """
    return obstacles


def create_obstacles(min_x, min_y, max_x, max_y):
    global obstacles
    draw_lines(-60, -100, -60, 100)
    draw_lines(-60, 100, -10, 100)
    draw_lines(10, 100, 56, 100)
    draw_lines(60, 100, 60, -100)

    draw_lines(60, -120, -64, -120)

    draw_lines(96, 196, 96, 30)
    draw_lines(96, -30, 96, -200)
    draw_lines(-100, 196, -100, 30)
    draw_lines(-100, -30, -100, -200)
    draw_lines(-100, -200, -30, -200)
    draw_lines(30, -200, 94, -200)
    draw_lines(-100, 196, -30, 196)
    draw_lines(30, 196, 94, 196)
    

    draw_lines(-30, -60, -30, 60)
    draw_lines(30, -60, 30, 60)

    draw_lines(-60, 140, 64, 140)
    return obstacles


def draw_lines(x, y, new_x, new_y):
    if x == new_x:
        if new_y > y:
            while new_y > y:
                obstacles.append(tuple((x,y)))
                y += 4
        if new_y < y:
            while new_y < y:
                obstacles.append(tuple((x,y)))
                y -= 4
    if y == new_y:
        if new_x > x:
            while new_x > x:
                obstacles.append(tuple((x,y)))
                x += 4
        if new_x < x:
            while new_x < x:
                obstacles.append(tuple((x,y)))
                x -= 4


def is_position_blocked(position_x, position_y):
    """
    Function compares the new position of the robot to obstacles
    if an obstacle is within the coordonates of the robots new position True is returned
    """

    for obs in obstacles:
        for x in range(obs[0], (obs[0]+5)):
            for y in range(obs[1], (obs[1]+5)):
                if position_x == x and position_y == y:
                    return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    function will loop through each iteration of coordonates and compare them to obstacles with the same coordonates
    if an obstacle is found to be in between old position and new position True is returned
    """
    
    if x1 == x2:
        coords = sorted([y1, y2])
        for location in range(coords[0], (coords[1] + 1)):
            if is_position_blocked(x1, location):
                return True
    if y1 == y2:
        coords = sorted([x1, x2])
        for location in range(coords[0], (coords[1] + 1)):
            if is_position_blocked(location, y1):
                return True