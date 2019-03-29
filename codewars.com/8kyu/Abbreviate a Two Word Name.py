'''Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
'''


def abbrevName(name):
    x, y = name.split()
    return '{}.{}'.format(x[0].upper(), y[0].upper())


'''
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
'''