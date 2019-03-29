# Move the first letter of each word to the end of it, then add "ay" to the end of the word.Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool')  # igPay atinlay siay oolcay
# pig_it('Hello world !')  # elloHay orldWay !


def pig_it(text):
    b = ''
    for i in text.split(' '):
        if i.isalpha():
            z = i[1:] + i[0] + 'ay'
            b += z + ' '
        else:
            b += i
    return b.rstrip()

#
# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())