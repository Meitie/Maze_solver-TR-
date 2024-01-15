import sys, os

USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
# sys.path.insert(0, USER_PATHS + "/")
# print("USRP", USER_PATHS)
dirlist = os.listdir(USER_PATHS)
py_index = dirlist.index("__pycache__")
dirlist.pop(py_index)
init_index = dirlist.index("__init__.py")
dirlist.pop(init_index)
all_mazes = ''.join(dirlist)
all_mazes = all_mazes.split(".py")
all_mazes.pop()

from import_helper import dynamic_import


maze_load = dynamic_import("maze.obstacles")

if len(sys.argv) > 2:
    if sys.argv[2] in all_mazes:
        maze_load = dynamic_import(f"maze.{sys.argv[2]}")