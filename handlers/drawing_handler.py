from models.map import Map


def draw_map(map: Map):
    print("-" * (map.cols * 2 + 1))
    for row in map.cell_grid:
        row_string = ""
        for cell in row:
            row_string += f"|{cell.display_sign}"
        print(row_string + "|")
        print("-" * (map.cols * 2 + 1))
        row_string = ""

def draw_help():
    print(
        """
        T -> toggle cell
        G -> generate random map
        N -> next generation
        """
    )


def clear_screen():
    print("\033c")
