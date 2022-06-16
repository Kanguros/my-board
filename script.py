import logging

from board_generator import BoardRenderer

logging.basicConfig(level="DEBUG")

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    DATA_FILE = "./links.yaml"
    OUTPATH = "./dashboard/dashboard.html"

    logger.info(f"Used variables: "
                f"Data file: {DATA_FILE} | "
                f"Output folder: {OUTPATH}")

    logger.info(f"Initialize Board creator...")
    board = BoardRenderer(DATA_FILE)
    logger.info(f"Initialized. Rendering the Dashboard")
    board_path = board.render(OUTPATH)
    logger.info(f"Created at: {board_path}")
