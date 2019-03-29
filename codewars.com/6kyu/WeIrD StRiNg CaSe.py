'''Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''


def to_weird_case(string):
    a = string.split(' ')
    slovo = []
    for i in a:
        z = ''
        for x in range(len(i)):
            if x % 2 == 0:
                z += i[x].upper()
            else:
                z += i[x].lower()
        slovo.append(z)

    return ' '.join(slovo)


print(to_weird_case('alag fsfsa yusss'))