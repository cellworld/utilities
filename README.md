# Instructions for New World Creation 
You can check the outputs of the executable files using XXX




Relevant Scripts and what they produce:<br>
1. XXXXXX
2. create_robot_occlusions.cpp -> (hexagonal.00_00.occlusions.robot)
3. create_paths.cpp -> (hexagonal.00_00.astar, hexagonal.00_00.astar.robot)
4. create_visibility.cpp -> (hexagonal.00_00.cell_visibility)
5. create_spawn_locations.cpp -> (hexagonal.00_00.spawn_locations)
    1. note: need to run steps 3 & 4 first  
<br>

Deliverables to be added to cellworld data:
<div style="font-family: monospace; white-space: pre;">
cellworld_data
├── cell_group
│   ├── hexagonal.00_00.occlusions
│   ├── hexagonal.00_00.occlusions.robot
│   ├── hexagonal.00_00.predator_destinations
│   └── hexagonal.00_00.spawn_locations
├── paths
│   ├── hexagonal.00_00.astar (needed for simulation only)
│   └── hexagonal.00_00.astar.robot
└── graph
    └── hexagonal.00_00.cell_visibility
</div>



1. git clone https://github.com/cellworld/utilities
2. cd utilities/scripts (echo $CELLWORLD_CACHE)
      1. ./build_utilities
      2. ./create_world
      3. ./prep_world 00_00 -f


