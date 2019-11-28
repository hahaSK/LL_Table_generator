"""
Created by Juraj Lahvička, xlahvi00
"""

from definitions import *

empty = {}


def init_empty():
    for non_terminal in non_terminals:
        empty[non_terminal] = empty_set


def get_empty():
    rules_dict = get_rules_set_dict()
    for non_terminal in non_terminals:
        for gram in rules_dict[non_terminal]:
            if gram.__contains__('ε'):
                empty[non_terminal] = epsilon
