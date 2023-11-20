import matplotlib.pyplot as plt
from cellworld import *

occlusions = "21_05"  # input new world occlusions
imp = 'hexagonal' # robot
world = World.get_from_parameters_names(imp, "canonical", occlusions)
map = Cell_map(world.configuration.cell_coordinates)
free_cell_ids = world.cells.free_cells().get('id')   # free cells in world
d = Display(world, background_color = 'white', cell_edge_color = 'lightgrey', habitat_edge_color='lightgrey')

def display_new_world():
    """
    Check new map
    """
    plt.show()
def check_cells(ids):
    """
    Use this to make sure the cells "blocked" from the robot are correct.
    The cyan cells are occluded in the map used to create the robot A* paths.
    """
    for i in ids:
        d.circle(world.cells[i].location, radius = 0.01, color = 'cyan')
    plt.show()


# call uncomment code based on desired test
# 1. Display new world
# display_new_world()

# 2. Display robot occlusions -> run create_robot_occlusions.cpp and assign output list to ids variable
# occlusion_ids = [3,18,20,24,27,34,36,48,58,68,78,82,93,116,121,123,131,141,142,152,153,157,160,163,164,171,174,176,181,204,211,227,230,232,237,238,245,248,249,255,260,265,266,276,286,292,313,317,321,325]
# check_cells(occlusion_ids)

# 3. Display robot destinations -> run create_predator_destinations.cpp
# destination_ids = [4,16,19,22,23,29,33,37,41,49,50,51,53,60,62,63,64,66,70,73,74,75,77,80,81,84,85,87,90,91,94,96,98,101,108,109,115,117,119,122,124,125,129,135,138,140,145,148,156,158,159,169,172,177,179,180,188,189,195,196,198,199,203,205,206,207,208,210,213,218,229,231,236,246,252,257,261,262,263,264,267,268,273,274,278,279,280,284,287,288,289,290,291,293,296,297,298,304,314,326]
# check_cells(destination_ids)

# 4. Display robot spawn locations -> run create_spawn_locations.cpp
# spawn_ids = [108,117,129,140,148,159,172,177,179,180,188,189,195,196,198,199,203,205,206,207,208,210,213,218,229,231,236,246,252,257,261,262,263,264,267,268,273,274,279,280,284,287,288,289,290,291,293,297,298,304,314,326]
# check_cells(spawn_ids)