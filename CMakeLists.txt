cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O0")

project(cellworld_utilities
        VERSION 2019.1.0
        DESCRIPTION "Cellworld Utilities Libraries"
        LANGUAGES CXX)

####
#### DEPENDENCIES
####

if (NOT EXISTS ${CMAKE_BINARY_DIR}/DependenciesConfig.cmake)
    file(DOWNLOAD https://raw.githubusercontent.com/germanespinosa/dependencies/main/DependenciesConfig.cmake ${CMAKE_BINARY_DIR}/DependenciesConfig.cmake)
endif()
set(Dependencies_DIR "${CMAKE_BINARY_DIR}")
find_package (Dependencies REQUIRED)

####
####
####

install_git_dependency(Thread_pool
        https://github.com/cellworld/dependency_thread_pool
        INCLUDE_DIRECTORIES include)


install_git_dependency(Params-cpp
        https://github.com/cellworld/dependency_params-cpp
        CMAKE_PROJECT
        IMPORT_TARGETS params-cpp)


#string(APPEND CMAKE_CXX_FLAGS " -fno-strict-aliasing -pthread")


install_git_dependency(Cellworld
        https://github.com/cellworld/cellworld
        PRIVATE
        CMAKE_PROJECT
        IMPORT_TARGETS cellworld)


message("Cellworld_IMPORTED_TARGETS: ${Cellworld_IMPORT_TARGETS}")


add_executable(create_lppos src/create_lppos.cpp)

target_link_libraries( create_lppos
        PRIVATE
        cellworld params-cpp)

add_executable(create_options src/create_options.cpp)

target_link_libraries( create_options
        PRIVATE
        cellworld params-cpp)

add_executable(create_paths src/create_paths.cpp)

target_link_libraries( create_paths
        PRIVATE
        cellworld params-cpp)

add_executable(create_visibility src/create_visibility.cpp)

target_link_libraries( create_visibility
        PRIVATE
        cellworld params-cpp)

add_executable(create_robot_occlusions src/create_robot_occlusions.cpp)

target_link_libraries( create_robot_occlusions
        PRIVATE
        cellworld params-cpp)

add_executable(create_predator_destinations src/create_predator_destinations.cpp)

target_link_libraries( create_predator_destinations
        PRIVATE
        cellworld params-cpp)

add_executable(create_spawn_locations src/create_spawn_locations.cpp)

target_link_libraries( create_spawn_locations
        PRIVATE
        cellworld params-cpp)

add_executable(create_world_statistics src/create_world_statistics.cpp)

target_link_libraries( create_world_statistics
        PRIVATE
        cellworld params-cpp)
