import sys, os
USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
sys.path.insert(0, USER_PATHS)
# print(USER_PATHS)

from import_helper import dynamic_import

runner = dynamic_import("maze_runner.solver")