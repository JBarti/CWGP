from models.cell import Cell, get_next_cell_generation
from models.map import Map, _build_adjacency_dict, generate_random_map, get_next_map_generation
from handlers.drawing_handler import draw_map

from pprint import pprint

def main():
    random_map =  generate_random_map(5, 5)
    draw_map(random_map)

    # adjacency_dict = _build_adjacency_dict(random_map)

    # next_gen = get_next_map_generation(random_map)

    # print(next_gen.cell_grid)

if __name__ == "__main__":
    main()
