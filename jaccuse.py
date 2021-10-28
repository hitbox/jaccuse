"""
My take on Sweigart's J'Accuse!
"""

import argparse
import random
import time

class JAccuse:

    def __init__(self, seconds_to_solve):
        self.seconds_to_solve = seconds_to_solve

    def reset(self):
        self.start_time = None
        self.game_over_time = None
        # XXX
        # 2021-10-15: left off here, not feeling this but wanting to come back.
        # nvim session in `.session`.

    def run(self):
        self.start_time = time.time()
        game


def main(argv=None):
    """
    """
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)

    jaccuse = JAccuse()
    jaccuse.reset()

if __name__ == '__main__':
    main()
