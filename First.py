"""
Created by Juraj Lahvička, xlahvi00
"""

from definitions import *

first = {}


def init_first():
    for non_terminal in non_terminals:
        first[non_terminal] = []


def check_first(non_terminal, line):
    split_line = line.split(' ')
    if terminals.__contains__(split_line[0].strip()):
        first[non_terminal] += [split_line[0]]
    elif non_terminals.__contains__(split_line[0]):
        first[non_terminal] += first[split_line[0]]


def _get_first():
    rules_dict = get_rules_set_dict()
    for non_terminal in non_terminals:
        for gram_line in rules_dict[non_terminal]:
            check_first(non_terminal, gram_line)


def remove_duplicates():
    for key in first:
        first[key] = list(dict.fromkeys(first[key]))


def get_first():
    _get_first()
    _get_first()
    remove_duplicates()
