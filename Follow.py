"""
Created by Juraj Lahvička, xlahvi00
"""

from definitions import *
from Empty import empty
from First import first

follow = {}


def init_follow():
    for non_terminal in non_terminals:
        follow[non_terminal] = []
    follow[S] = '$'


def find_non_terminals_indexes(split_line):
    indexes = []
    for i, term in enumerate(split_line):
        if term in non_terminals:
            indexes.append(i)
    return indexes


def get_term_index_follow(non_terminal, index, split_line):
    non_term_searched = split_line[index]
    for current_index in range(index + 1, split_line.__len__() + 1):
        if current_index >= split_line.__len__():
            follow[non_term_searched] += follow[non_terminal]
            return

        if split_line[current_index] in non_terminals:
            follow[non_term_searched] += first[split_line[current_index]]
            if empty[non_term_searched] == empty_set:
                return
            else:
                continue
        if split_line[current_index] in terminals:
            follow[non_term_searched] += [split_line[current_index]]
            return
        else:
            raise Exception("Follow: " + split_line[current_index] +
                            " not found in any set.Searched for " +
                            non_term_searched + ". Left side of rule: "
                            + non_terminal)


def check_follow(non_terminal, gram_line):
    split_line = gram_line.split(' ')
    non_terminal_indexes = find_non_terminals_indexes(split_line)
    for index in non_terminal_indexes:
        get_term_index_follow(non_terminal, index, split_line)


def _get_follow():
    rules_dict = get_rules_set_dict()
    for non_terminal in non_terminals:
        for gram_line in rules_dict[non_terminal]:
            check_follow(non_terminal, gram_line)


def remove_duplicates():
    for key in follow:
        follow[key] = list(dict.fromkeys(follow[key]))


def get_follow():
    _get_follow()
    _get_follow()
    _get_follow()
    _get_follow()
    remove_duplicates()
