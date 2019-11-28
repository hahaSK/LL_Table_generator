"""
Created by Juraj Lahvička, xlahvi00
"""

from definitions import *
from Predict import predicts

table = {}
rows = non_terminals
columns = terminals


def init_table():
    for line_num in range(rules.__len__()):
        table[line_num] = []


def print_table():
    print('', end='\t')
    for column in columns:
        if column == expression:
            column = '$'
        print(column, end='\t')
    print('', end='\n')
    for row in rows:
        print(row, end='\t')
        for column in columns:
            values_in_cell = ''
            for cell_key in table:
                non_term_term_pair_wanted = (row, column)
                for non_term_term_pair in table[cell_key]:
                    if non_term_term_pair == non_term_term_pair_wanted:
                        if values_in_cell != '':
                            predict_number = cell_key + 1
                            values_in_cell += ',' + predict_number.__str__()
                        else:
                            predict_number = cell_key + 1
                            values_in_cell += predict_number.__str__()
            print(values_in_cell, end='\t')
        print('', end='\n')


def set_table_cells():
    parsed_rules = get_rules_lr_parsed()
    for predict in predicts:
        left_side = parsed_rules[predict][0]
        for terminal in predicts[predict]:
            table[predict] += [(left_side, terminal)]


def make_table():
    init_table()
    set_table_cells()
    print_table()
