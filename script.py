import sys

from board_generator import BoardRenderer

if __name__ == '__main__':
    args = sys.argv[1:]
    DATA_FILE = "./links.yaml"
    OUTPATH = "./dashboard/dashboard.html"

    print(f"Initialize Board class")
    board = BoardRenderer(DATA_FILE)
    print(f"Initialized. Renderng")
    board_path = board.render(OUTPATH)
    print(f"Created at: {board_path}")