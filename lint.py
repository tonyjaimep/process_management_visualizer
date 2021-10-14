import argparse
import logging
import sys
from pylint.lint import Run


logging.getLogger().setLevel(logging.INFO)

parser = argparse.ArgumentParser(prog="LINT")

parser.add_argument(
    "-p",
    "--path",
    help="path to directory you want to run pylint | "
    "Default: %(default)s | "
    "Type: %(type)s ",
    default="./src",
    type=str,
)

parser.add_argument(
    "-t",
    "--threshold",
    help="score threshold to fail pylint runner | "
    "Default: %(default)s | "
    "Type: %(type)s ",
    default=7,
    type=float,
)

args = parser.parse_args()
PATH = str(args.path)
THRESHOLD = float(args.threshold)

logging.info("PyLint Starting | " "Path: %s | " "Threshold: %s " % (PATH, THRESHOLD))

results = Run([PATH], do_exit=False)

FINAL_SCORE = results.linter.stats["global_note"]

if FINAL_SCORE < THRESHOLD:
    MESSAGE = (
        "PyLint Failed | " "Score: %s | " "Threshold: %s " % (FINAL_SCORE, THRESHOLD)
    )

    logging.error(MESSAGE)
    raise Exception(MESSAGE)

MESSAGE = "PyLint Passed | " "Score: %f | " "Threshold: %f " % (FINAL_SCORE, THRESHOLD)

logging.info(MESSAGE)
