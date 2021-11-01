from typing import Callable
from models.map import Map

_COMMANDS = {}

def execute_command():
    inputed_command = input("What is your next command: ")

    if inputed_command in _COMMANDS:
        _COMMANDS[inputed_command]()


def handle_toggle_cell(callback: Callable, map: Map):
    cell_position = input("What is the cell position (x y)")
    cell_column, cell_row = cell_position.split(" ")
    cell_column = int(cell_column)
    cell_row = int(cell_row)

    return callback(cell_row, cell_column, map)



def handle_get_next_gen(callback: Callable, map: Map):
    return callback(map)
