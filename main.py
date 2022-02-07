#! /usr/bin/env python

import sys
from functions.base import check_args

if __name__ == '__main__':
    # Force lowercase on passed arguments, remove script name (default first argument).
    args = [arg.lower() for arg in sys.argv[1:]]
    check_args(args)
