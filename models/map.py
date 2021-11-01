from typing import List
from random import choices

from .cell import Cell, get_next_cell_generation


class Map:
    def __init__(self, row_count: int, col_count: int, cell_grid: List[List[Cell]]):
        self.rows = row_count
        self.cols = col_count
        self.cell_grid = cell_grid


def _get_adjacent_cell_indexes(current_row, current_col, row_count, col_count):
    adjacent_indexes = [
        (current_row, current_col + 1),
        (current_row + 1, current_col),
        (current_row + 1, current_col + 1),

        (current_row - 1, current_col),
        (current_row, current_col - 1),
        (current_row - 1, current_col - 1),

        (current_row + 1, current_col - 1),
        (current_row - 1, current_col + 1),
    ]

    filtered_adjacent_index_pairs = []
    for index_pair in adjacent_indexes:
        if -1 in index_pair:
            continue
        elif row_count in index_pair:
            continue
        elif col_count in index_pair:
            continue

        filtered_adjacent_index_pairs.append(index_pair)

    return filtered_adjacent_index_pairs


def _build_adjacency_dict(map: Map):
    adjacency_dict = {}

    for row_number in range(map.rows):
        for col_number in range(map.cols):
            adjacent_indexes = _get_adjacent_cell_indexes(
                row_number,
                col_number,
                map.rows,
                map.cols
            )

            current_cell = map.cell_grid[row_number][col_number]

            adjacent_cells = [
                map.cell_grid[index_pair[0]][index_pair[1]]
                for index_pair in adjacent_indexes
            ]

            adjacency_dict[current_cell] = adjacent_cells

    return adjacency_dict
    

def generate_random_map(rows: int, cols: int):
    random_cell_death_matrix = [
        choices(population=[True, False], weights=[3, 1], k=cols)
        for row in range(rows)
    ]

    map_cells = [
        [
            Cell(is_dead=random_cell_death_matrix[row][col])
            for col in range(cols)
        ]
        for row in range(rows)
    ]

    new_map = Map(
        row_count=rows,
        col_count=cols,
        cell_grid=map_cells,
    )

    return new_map

def get_next_map_generation(map: Map):
    # generiramo tablicu bliskosti
    adjacency_dict = _build_adjacency_dict(map)
    
    # nova matrica čelija di su sve čelije mrtve
    new_map = [[Cell(is_dead=True)] * map.cols] * map.rows


    # prolazimo kroz svaku čeliju stare mape
    # dohvacamo njene okolne celije
    # stvaramo celiju iduce generacije
    # ubacujemo je u "new_map"
    for row in range(map.rows):
        for col in range(map.cols):
            current_cell = map.cell_grid[row][col]
            adjacent_cells = adjacency_dict[current_cell]
            next_cell_gen = get_next_cell_generation(current_cell, adjacent_cells)
            new_map[row][col] = next_cell_gen

    return Map(
        row_count=map.rows,
        col_count=map.cols,
        cell_grid=new_map,
    )
