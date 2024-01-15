import sys
import maze_runner.solver as solve          # hard import to stop importing loop
from maze import maze_load as maze_load
from maze import all_mazes as all_mazes
from world import worlds as world



valid_command = ['off', 'help', 'left', 'right', 'history', 'reset','forward', 'back', 'sprint', 'replay', 'mazerun']
replay_flags = ['silent', 'reversed', 'reversed silent']
mazerun_flags = ['left', 'right', 'top', 'bottom']
history = []
silent = False

def get_robot_name():
    """
    Asks for an input from the user, checks if the user submitted a name or not
    :returns: The name from the user
    """

    name = input("What do you want to name your robot? ")

    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_user_command(robot_name):
    """
    Asks the user provide a command for the robot, checks if it is valid or not
    :returns: The users command in lower case
    """
    
    command = input(f"{robot_name}: What must I do next? ")
    while len(command) == 0 or not valid_commands(command):
        output(robot_name, f"Sorry, I did not understand '{command}'.")
        command = input(f"{robot_name}: What must I do next? ")
    return command.lower()


def split_commands(command):
    """
    Splits the string at the first space character, to get the actual command.
    As well as the argument(s) in second position.
    :returns: arguments[0] = command, arguments[1] = the movement or ''"
    """

    arguments = command.split(' ', 1)
    if len(arguments) > 1:
        return arguments[0], arguments[1]
    return arguments[0], ''


def order_flags(argument):
    """
    Checks the arguments that exist and orders them based on what was passed
    :returns: correct order of the arguments
    """

    if 'silent' in argument and 'reversed' not in argument:
        return 'silent'
    elif 'silent' not in argument and 'reversed' in argument:
        return 'reversed'
    elif 'silent' in argument and 'reversed' in argument:
        return 'reversed silent'
    return ' '.join(argument)


def args_splitter(arg):
    """
    Takes in the arguments from silent, finds any number inside it and pops it
    out and appends it to the end, as well as checks if there is a dash inside
    of the argument
    """

    # Sets up some used vars
    digit = int()
    dig_check = 0
    new_arg = []
    argument = arg.split(' ')

    if len(argument) > 1:
        for i in argument:
            if i.isdigit() or '-' in i:     # checks if "i" isdigit or has '-'
                digit = argument.index(i)
                dig_check += 1              # show that there is a digit
        if dig_check == 0:                  # checks if there was digit
            flags = order_flags(argument)   # ordering the flags
            return flags, ''                # shows and returns just flags
        else:
            num = argument.pop(digit)       # removes the number from list
            flags = order_flags(argument)   # orders the flags
            new_arg.append(flags.lower())   # appends the flags
            new_arg.append(num)             # appends the numbers
            return new_arg[0], new_arg[1]
    else:
        for i in argument:                  # for each item in argument
            if i.isdigit() or '-' in i:     # checks if "i" isdigit or has '-'
                return '', i                # returns '', and the number
        return argument[0], ''              # else returns argument, ''


def split_on_dash(arg):
    """
    Splits the arg on the '-', if there is a non digit inside after the split,
    :returns: True and False (false represents that its not a valid command)
    :returns: if good the number in position 1 and position 2 
    """

    argument = arg.split('-')
    for x in argument:
        if not x.isdigit():
            return True, False
    return argument[0], argument[1]


def valid_commands(command):
    """
    Checks if the command is inside the valid commands list or not.
    :returns: True if it is valid
    :returns: False if it is invalid
    """

    (command_name, arg) = split_commands(command)

    # checks if any of the arg contain a digit as well
    # for combining flags and numbers
    flag_and_digit = False
    for x in arg:
        if x.isdigit(): flag_and_digit = True

    # Checks if user command is valid, or if arg is non existant, or if it is an
    # int or if the flags given are words or if there is flags and numbers
    return command_name.lower() in valid_command and (len(arg) == 0 or is_int(arg) or (order_flags(arg) in replay_flags) or flag_and_digit == True or arg in mazerun_flags)


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :returns: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def output(name, message):
    """
    Prints out the message given 2 arguments
    :returns: a print of the name and message
    """
    
    return print(f"{name}: {message}")


def show_help():
    """
    Provides help information for the user
    :returns: (True, 'help information')
    """

    help_info = """I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\nFORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\nBACK - move backward by specified number of steps, e.g. 'BACK 10'\nRIGHT - turn right by 90 degrees\nLEFT - turn left by 90 degrees\nSPRINT - sprint forward according to a formula\nREPLAY - Redo all the steps in the history\nREPLAY SILENT - Redo all the steps in the history but supress the movements only returning the output\nMAZERUN - The robot will complete the maze, and make it to the outside"""
    return True, help_info


def add_history(command):
    """
    Checks if either 'replay'/'silent'/'reversed' are in the command, if they
    are ignore them, else append the command to the history
    :returns: history
    """

    global history

    if "replay" in command or "silent" in command or "reversed" in command or 'history' in command or 'reset' in command:
        return history
    else:
        history.append(command)
        return history


def call_history():
    """
    :returns: True, call to list of everything in history
    """
    return True, history


def do_replay(robot_name, arg, silence, reverse):
    """

    """
    global silent

    (comms, nums) = args_splitter(arg)
    values = history
    output = ' commands.'

    if reverse == True:
        values = list(reversed(values))
    
    if silence == True:
        silent = True

    if silence == True and reverse == False:
        output = ' commands silently.'
    elif silence == False and reverse == True:
        output = ' commands in reverse.'
    elif silence == True and reverse == True:
        output = ' commands in reverse silently.'

    if nums:
        if not '-' in nums:                         # if no dash in argument
            if int(nums) > len(values):             # checks if arg > history
                return True, 'Sorry, Commands length exceeds history length'
            silent                                  # checking silence 
            for value in values[-int(nums):]:       # for each value run it
                handle_command(robot_name, value)   # do each movement
            silent = False                          # reseting silent
            return True, f" > {robot_name} replayed {str(int(nums))}{output}"
        else:
            (arg1, arg2) = split_on_dash(nums)       # splitting on the '-'
            if int(arg1) > len(nums):               # checks the lenght is good
                return True, 'Sorry, Commands length exceeds history length'
            if arg2 == False:                       # means not understood
                return False, f"{robot_name}: : Sorry, I did not understand 'replay {arg}'.'"
            silent                                  # setting the silence
            for value in values[-int(arg1):-int(arg2)]:     # moves from num-num
                handle_command(robot_name, value)
            silent = False                          # reseting silent
            return True, f" > {robot_name} replayed {str(int(arg1) - int(arg2))}{output}"
    else:                                           # there was no arg
        silent                                      # silent check
        print(f"silent {silent}")
        for value in values:                        # for each normal replay run
            handle_command(robot_name, value)
        silent = False                              # resetting silent

        return True, f" > {robot_name} replayed {str(len(history))}{output}"


def replay_passer(robot_name, arg):
    """
    Checks the args for which commands will be passed into replay
    silent and reveresed, stating if they are true or false.
    :returns: A call to the do_replay function
    """
    commands, nums = args_splitter(arg)

    if commands == '':
        return do_replay(robot_name, arg, False, False)
    elif commands == 'silent':
        return do_replay(robot_name, arg, True, False)
    elif commands == 'reversed':
        return do_replay(robot_name, arg, False, True)
    elif commands == 'reversed silent':
        return do_replay(robot_name, arg, True, True)


def handle_command(robot_name, command):
    """
    Handles the command from the users, checks it if is valid and what each 
    command should do
    :returns: True if the robot must continue after each command
    :returns: False if the robot must turn off
    """

    (command_name, arg) = split_commands(command)

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = show_help()
    elif command_name == 'history':
        do_next, command_output = call_history()
    elif command_name == 'reset':
        full_reset()
        do_next, command_output = True, f"{robot_name} has reset."
    elif command_name == 'right':
        (do_next, command_output) = world.turn_right(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = world.turn_left(robot_name)
    elif command_name == 'forward':
        (do_next, command_output) = world.do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = world.do_back(robot_name, int(arg))
    elif command_name == 'sprint':
        (do_next, command_output) = world.sprint(robot_name, int(arg))
    elif command_name == 'replay':
        (do_next, command_output) = replay_passer(robot_name, arg)
    elif command_name == 'mazerun':
        (do_next, command_output) = solve.maze_solver(robot_name, arg)

    if silent == True:                      # check if silent is true
        return do_next                      # do next, withough printing command
    else:                                   # if silent not true
        print(command_output)               # print output
        if do_next == True:                 # check if do_next is true (replay)
            world.show_position(robot_name) # show position
        do_next = True                      # set do next true
        return do_next


def full_reset():
    """
    Resets all globals and positions that are updateable
    """

    history = []
    silent = False
    world.position_x = 0
    world.position_y = 0
    world.current_direction_index = 0


def robot_start():
    """
    Calls the start of the robot and runs all the commands to get everything
    going, calls all other functions allowing for the robot to run.
    :shuts down if off is the command:
    """

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    full_reset()

    if len(sys.argv) == 3 and sys.argv[2] in all_mazes:
        print(f"{robot_name}: Loaded {sys.argv[2]}.")
        if not sys.argv[1] == "turtle":
            world.show_obstacles()
    elif len(sys.argv) == 2:
        if not sys.argv[1] == "turtle":
            print(f"{robot_name}: Loaded obstacles.")
            world.show_obstacles()
    else:
        print(f"{robot_name}: Loaded obstacles.")
        world.show_obstacles()


    command = get_user_command(robot_name)
    while handle_command(robot_name, command):
        add_history(command)
        command = get_user_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()