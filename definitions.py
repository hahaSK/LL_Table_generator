"""
Created by Juraj Lahvička, xlahvi00
"""

epsilon = 1     # ε
empty_set = 2   # Ø

non_terminals = ['<human>', '<command_list>', '<command>', '<animal>', '<dog>', '<cat>', '<call>']  # '<expression>']

S = non_terminals[0]    # End state

expression = '<expression>' # this is used in table, where expression is replaced with $

terminals = ['woof', 'meow', 'chrrrrr', '(', ')', 'sit', 'bark', 'stay', 'new_day', 'come', 'die', '<expression>']


"""
All the terminals and non terminals need to be separated by space, so the line/rule is split correctly.
For example: '(<exp>)' this first of this will be '(<exp>)', which is incorrect => '( <exp> )' now the 
first will be '(' => OK
"""
rules = ['<human> → <command_list> die',
         '<command_list> → <command> new_day <command_list>',
         '<command-list> → new_day <command>',
         '<command_list> → ε',

         '<command> → sit <animal>',
         '<command> → bark <animal>',
         '<command> → stay <animal>',
         '<command> → <expression>',
         '<command> → <call>',
         
         '<animal> → <dog>',
         '<animal> → <cat>',

         '<dog> → woof',

         '<cat> → meow',
         '<cat> → chrrrrr',

         '<call> → come ( <animal> )'
         ]


def get_rules_set_dict():
    _rules = dict()
    for rule in rules:
        rule_split = rule.split('→')
        rule_left = rule_split[0].strip()
        if not _rules.__contains__(rule_left):
            _rules[rule_left] = [rule_split[1].strip()]
        else:
            _rules[rule_left] += [rule_split[1].strip()]

    return _rules


def get_rules_lr_parsed():
    _rules = list()
    for rule in rules:
        rule_split = rule.split('→')
        _rules += [(rule_split[0].strip(), rule_split[1].strip())]
    return _rules
