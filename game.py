from pprint import pprint

from handlers.drawing_handler import draw_map, clear_screen
from handlers.input_handler import handle_toggle_cell, execute_command, handle_get_next_gen
from models.cell import Cell, get_next_cell_generation
from models.map import (
    Map,
    _build_adjacency_dict,
    generate_random_map,
    get_next_map_generation,
    toggle_map_cell,
)


def on_toggle_cell(cell_row: int, cell_col: int, map: Map):
    return toggle_map_cell(map, cell_row, cell_col)


def on_next_generation(map: Map):
    return get_next_map_generation(map)


def main():
    random_map =  generate_random_map(12, 12)
    clear_screen()
    draw_map(random_map)

    while True:
        command = input("Next command: ")
        if command == "T":
            random_map = handle_toggle_cell(on_toggle_cell, random_map)
        elif command == "N":
            random_map = handle_get_next_gen(on_next_generation, random_map)
            draw_map(random_map)

        clear_screen()
        draw_map(random_map)


if __name__ == "__main__":
    main()
