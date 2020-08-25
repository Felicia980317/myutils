import logging
import sys
from datetime import datetime

import numpy as np


class ProgressBar(object):
    @staticmethod
    def start(total_iteration):
        ProgressBar.total_iteration_ = total_iteration
        ProgressBar.start_time_ = datetime.now()

    @staticmethod
    def status(iteration, length=30, **kwargs):
        time_total = (datetime.now() - ProgressBar.start_time_).seconds
        time_eta = (time_total / iteration) * (ProgressBar.total_iteration_ - iteration)

        num_current = iteration / ProgressBar.total_iteration_
        num_current = int(num_current * length)
        num_future = length - num_current

        string_progress = ""
        if not (iteration == ProgressBar.total_iteration_):
            string_progress = "%d/%d [%s%s] eta:%3ds," % (
                iteration,
                ProgressBar.total_iteration_,
                ">" * num_current,
                "-" * num_future,
                time_eta,
            )
        else:
            string_progress = "%d/%d [%s%s]     %3ds," % (
                iteration,
                ProgressBar.total_iteration_,
                ">" * num_current,
                "-" * num_future,
                time_total,
            )

        string_out = ""
        for key in kwargs.keys():
            string_out += " %s: %1.8f," % (key, kwargs[key])

        string_out = "\r" + string_progress + string_out
        # print(string_out)
        sys.stdout.write(string_out)
        sys.stdout.flush()
        if iteration == ProgressBar.total_iteration_:
            sys.stdout.write("\n")


def getLogger(name, path):
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(path + "/log.txt")
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    return logger


if __name__ == "__main__":
    while True:
        ProgressBar.start(100000)
        for i in range(100000):
            ProgressBar.status(i + 1, a=2, c=4)
            import time

            time.sleep(1)
