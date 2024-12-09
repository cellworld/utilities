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
    auto occlusions = p.get(Key("-o","--occlusions"),"20_05");
    auto configuration = p.get(Key("-c","--configuration"),"hexagonal");
    bool robot_paths = p.contains(Key("-r"));

    auto robot_occlusions = Cell_group_builder::get_from_parameters_name("hexagonal",  occlusions, robot_paths?"occlusions.robot":"occlusions");
    World world = World::get_from_parameters_name(configuration,"canonical");
    Graph graph = world.create_graph();
    Paths paths = Paths::get_astar(graph);


    // saves to data directory
    fs::path exec_dir = fs::canonical(argv[0]).parent_path();
    fs::path data_dir = exec_dir / "../data/";
    fs::path save_path = data_dir / ("hexagonal." + occlusions + ".astar");
    paths.save(save_path.string());

    cout << paths << endl;
}

