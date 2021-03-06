#!/usr/bin/env python
import logging
from threading import Timer
logger = logging.getLogger(__name__)


class HomieTimer(object):
    """docstring for HomieTimer"""

    def __init__(self, t, hFunction):
        super(HomieTimer, self).__init__()
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def main():
    pass

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Quitting.")
