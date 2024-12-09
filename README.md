# Instructions to setup project and create a new world
Note: if you have already setup the project (meaning you have completed steps 1-3 previously) start at step 4 to create a new world.
### Step 1: Clone the Repository
```bash
git clone https://github.com/cellworld/utilities
```
### Step 2: Set CELLWORLD_CACHE
Run the following commands to  
(1) navigate to scripts directory and  
(2) set CELLWORLD_CACHE and clone cellworld_data repository if the directory does not exist locally.

Note: I am assuming the cellworld_data repository exists in /mnt/c/Research. If it is located elsewhere, update the paths in the commands below accordingly.  
Note: if you get an error like this: /bin/bash^M: bad interpreter: No such file or directory, run:  
**dos2unix set_cellworld_cache**    
```bash
cd utilities/scripts
./set_cellworld_cache /mnt/c/Research
```
### Step 3: Build Project
```bash
./build_utilities
```
### Step4: Create World
```bash
./create_world
```
1. selected occluded cells
2. press 's' key
3. enter world name into terminal (e.g., 00_00)
4. press 'enter' key
4. press 'p' key (automatically runs ./prep_world for new world)
5. press 'q' key once the process is finished.

### Step 5: Prep Existing World
If the world already exists, skip Step 4 and run the following command:
```bash
./prep_world 00_00 -f
```
Note: Substitute "00_00" in the command above with the desired world name.

### Step 6: Commit to Github
Navigate to the cellworld_data project and commit all files to GitHub.

# Deliverables
Files added to cellworld data:
```
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
```

# Project Details
The following sections provide brief descriptions of files within the primary directories of this project.

## scripts directory
1. build_utilities: builds the project properly
2. set_cellworld_cache: The line sets the environment variable "CELLWORLD_CACHE" and clones cellworld_data repository is it doens't exist locally (the new world files will be saved there)
3. create_world: opens UI for creating a new world
4. prep world: runs all C++ files required to generate all cellworld_data for new world


## src directory
1. create_robot_occlusions.cpp -> (hexagonal.00_00.occlusions.robot)
2. create_paths.cpp -> (hexagonal.00_00.astar, hexagonal.00_00.astar.robot)
   1. note: need to run step 1 first
3. create_predator_destinations.cpp -> (hexagonal.00_00.predator_destinations)
3. create_visibility.cpp -> (hexagonal.00_00.cell_visibility)
4. create_spawn_locations.cpp -> (hexagonal.00_00.spawn_locations)
    1. note: need to run steps 3 & 4 first  

## python directory
1. create_world.py -> allows you to select occluded cells, save a new world, and run prep_world script
2. check_prep_world.py -> allows you to check output of (create_robot_occlusions.cpp, create_predator_destinations.cpp, and create_spawn_locations.cpp)


