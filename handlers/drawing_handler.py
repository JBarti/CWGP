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
