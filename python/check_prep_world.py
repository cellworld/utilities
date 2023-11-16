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
def check_robot_occlusions(ids):
    """
    Use this to make sure the cells "blocked" from the robot are correct.
    The cyan cells are occluded in the map used to create the robot A* paths.
    """
    for i in ids:
        d.circle(world.cells[i].location, radius = 0.005, color = 'cyan')
    plt.show()


# call function based on desired test
# 1. Display new world
# display_new_world()

# 2. Display robot occlusions
ids = [3,18,20,24,27,34,36,48,58,68,78,82,93,116,121,123,131,141,142,152,153,157,160,163,164,171,174,176,181,204,211,227,230,232,237,238,245,248,249,255,260,265,266,276,286,292,313,317,321,325]
check_robot_occlusions(ids)
