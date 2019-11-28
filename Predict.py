"""
Created by Juraj Lahvička, xlahvi00
"""

from Follow import follow
from First import first
from Empty import empty
from definitions import *

predicts = {}


def init_predict():
    for line_num in range(rules.__len__()):
        predicts[line_num] = []


def check_predict(rule_number, non_terminal, gram_line):
    terms_in_line = gram_line.split(' ')
    for term in terms_in_line:
        if term.__contains__('ε'):
            predicts[rule_number] += follow[non_terminal]
            return
        if term in terminals:
            predicts[rule_number] += [term]
            return
        if term in non_terminals:
            predicts[rule_number] += first[term]
            if empty[term] == empty_set:
                return
            continue
        else:
            raise Exception("Term: " + term + " not found in any set. " +
                            "Rule number: " + rule_number.__str__() + '\n' +
                            "Rule: " + rules[rule_number])


def _get_predict():
    parsed_rules = get_rules_lr_parsed()
    for rule_number, rule in enumerate(parsed_rules):
        check_predict(rule_number, rule[0], rule[1])


def remove_duplicates():
    for key in predicts:
        predicts[key] = list(dict.fromkeys(predicts[key]))


def get_predict():
    _get_predict()
    _get_predict()
    remove_duplicates()
