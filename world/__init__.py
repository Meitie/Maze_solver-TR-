import sys
from import_helper import dynamic_import

worlds = dynamic_import("world.text.world")

if len(sys.argv) > 1:
    if sys.argv[1] == "turtle":
        worlds = dynamic_import("world.turtle.world")