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

# Instructions to create a new world
### Step 1: Clone the Repository
```bash
git clone https://github.com/cellworld/utilities
```
### Step 2: Configure Cellworld Cache
Run the following commands (1) navigate to scripts directory  and (2) to set up the Cellworld cache and clone cellworld_data repository if the directory "${folder}/cellworld_data" does not exist.
```bash
git clone https://github.com/cellworld/utilities
```
1. git clone https://github.com/cellworld/utilities
2. cd utilities/scripts (echo $CELLWORLD_CACHE)
   1. ./set_cellworld_cache
   2. ./build_utilities
   3. ./create_world
      1. selected occluded cells 
      2. press s key
      3. enter world name into terminal (like 00_00)
      4. press enter key
      4. press p key (automatically runs ./prep_world for new world)
      5. press q key (once the process is finished)
   4. Alternatively, if the world is already skip step 3 and run: ./prep_world 00_00 -f
      1. Note: subst. 00_00 in the command above for desired world name
   5. Navigate to cellworld_data project and commit all files to github 


