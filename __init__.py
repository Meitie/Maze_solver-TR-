import os, sys

USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
print("USRP", USER_PATHS)
sys.path.insert(0, USER_PATHS + "/")
dirlist = os.listdir(USER_PATHS)
print(dirlist)