#include <cell_world.h>
#include <params_cpp.h>
#include <filesystem>

using namespace params_cpp;
using namespace cell_world;
using namespace std;
using namespace json_cpp;
namespace fs = std::filesystem;


int main (int argc, char **argv){
    Parser p(argc,argv);
    auto occlusions = p.get(Key("-o","--occlusions"),"21_05");
    World world = World::get_from_parameters_name("hexagonal","canonical", occlusions);
    Graph graph = world.create_graph();
    Cell_group cells = world.create_cell_group().free_cells();
    Graph g = world.create_graph();
    Cell_group pd;
    for (const Cell &cell:cells) {
        if (graph.is_connected(cell,world.cells[0]) && g[cell].size() == world.connection_pattern.size()){  // if the cell is connected to the entrance and surrounded by free cells add it to destination list
            pd.add(cell);
        }
    }

    // saves to data directory
    fs::path exec_dir = fs::canonical(argv[0]).parent_path();
    fs::path data_dir = exec_dir / "../data/";
    fs::path save_path = data_dir / ("hexagonal." + occlusions + ".predator_destinations");
    pd.save(save_path.string());

    cout << pd.get_builder() << endl;
}

