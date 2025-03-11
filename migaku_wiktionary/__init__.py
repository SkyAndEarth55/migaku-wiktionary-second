import sys

import progressbar


def is_in_test_environment():
    return "pytest" in sys.modules


# This is new file
# This is other file

if is_in_test_environment():
    ProgressBar = progressbar.NullBar
else:
    ProgressBar = progressbar.ProgressBar
