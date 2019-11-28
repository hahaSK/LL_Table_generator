"""
Created by Juraj Lahvička, xlahvi00
"""

from Empty import *
from First import *
from Follow import *
from Predict import *
from Table import *


def main():
    init_empty()
    get_empty()
    print("Empty:")
    print(empty)

    init_first()
    get_first()
    print("First:")
    print(first)

    init_follow()
    get_follow()
    print("Follow:")
    print(follow)

    init_predict()
    get_predict()
    print("Predict:")
    print(predicts)

    make_table()


if __name__ == '__main__':
    main()
