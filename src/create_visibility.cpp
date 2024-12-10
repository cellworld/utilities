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
    World world = World::get_from_parameters_name(configuration,"canonical", occlusions);
    Cell_group cells = world.create_cell_group();
    auto cell_shape = world.get_configuration().cell_shape;
    auto cell_transformation = world.get_implementation().cell_transformation;
    auto visibility = Coordinates_visibility::create_graph(cells,cell_shape,cell_transformation);

    // saves to data directory
    fs::path exec_dir = fs::canonical(argv[0]).parent_path();
    fs::path data_dir = exec_dir / "../data/";
    fs::path save_path = data_dir / ("hexagonal." + occlusions + ".cell_visibility");
    visibility.save(save_path.string());

    cout << visibility << endl;
}

