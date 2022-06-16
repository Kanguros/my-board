import logging
import os

from board_generator import BoardRenderer

logging.basicConfig(level="DEBUG")

logger = logging.getLogger(__name__)

if __name__ == '__main__':

    TEST_DATA_FILE = "./test_links.yaml"
    DATA_FILE = "./links.yaml"

    if os.path.exists(DATA_FILE):
        INPUT = DATA_FILE
    elif os.path.exists(TEST_DATA_FILE):
        INPUT = TEST_DATA_FILE
    else:
        raise ValueError(f"Missing data file. "
                         f"Not found in paths: {TEST_DATA_FILE} and {DATA_FILE}")

    OUTPATH = "./dashboard/dashboard.html"

    logger.info(f"Used variables: "
                f"Data file: {INPUT} | "
                f"Output folder: {OUTPATH}")

    logger.info(f"Initialize Board creator...")
    board = BoardRenderer(DATA_FILE)
    logger.info(f"Initialized. Rendering the Dashboard")
    board_path = board.render(OUTPATH)
    logger.info(f"Created at: {board_path}")
