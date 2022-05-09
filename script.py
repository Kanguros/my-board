from my_board.cli import Board

if __name__ == '__main__':
    DATA = "./data/links.yaml"
    TEMPLATE = "template"
    OUTPATH = "./data/dashboard.html"

    print(f"Initialize Board class")
    board = Board(DATA, TEMPLATE)
    print(f"Initialized. Renderng")
    board_path = board.render(OUTPATH)
    print(f"Created at: {board_path}")