from typing import List

CELL_SIGNS_BY_DEATH_STATE = {
    True: " ",
    False: "#",
}

class Cell:
    def __init__(self, is_dead: bool):
        self.is_dead = is_dead
        self.display_sign = CELL_SIGNS_BY_DEATH_STATE[is_dead]


def get_next_cell_generation(current_cell: Cell, adjacent_cells: List[Cell]):
    alive_cells_count = len([
        cell
        for cell in adjacent_cells
        if not cell.is_dead
    ])

    if alive_cells_count < 2:
        return Cell(is_dead=True)
    elif alive_cells_count == 2:
        return Cell(current_cell.is_dead)
    elif alive_cells_count == 3:
        return Cell(is_dead = False)
    else:
        return Cell(is_dead=True)
