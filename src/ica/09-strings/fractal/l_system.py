""""
Implementation of the Aristid Lindenmayer-system (L-systems)

@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""


def apply_l_system(dict_of_things):
    assert type(dict_of_things) is dict
    assert len(dict_of_things) == 3
    assert 'axiom' in dict_of_things and 'rules' in dict_of_things and 'n' in dict_of_things

    s = dict_of_things['axiom']
    for _ in range(dict_of_things['n']):
        s = apply_rules(s, dict_of_things['rules'])

    return s


def apply_rules(s: str, rules: dict):
    assert type(s) is str
    assert type(rules) is dict

    new_str = ''
    for c in s:
        rule_found = False
        for key in rules:
            if len(key) != 1:
                print("{} -> {} not supported, LHS is not of length "
                      "1".format(key, rules[key]))
                assert False
            if key == c:
                new_str += rules[key]
                rule_found = True
                break

        # no rule
        if not rule_found:
            new_str += c

    return new_str


if __name__ == "__main__":
    axiom = 'A'
    rules = {'A':'B', 'B':'AB'}

    for i in range(10):
        my_dict = {'axiom':axiom,'rules':rules,'n':i}
        print(apply_l_system(my_dict))
