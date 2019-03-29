# Description:
#
# Remove words from the sentence if it contains one exclamation mark. Words are separated by spaces in the sentence. Please remember, one.
#
# Examples
#
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


def remove(s):
    a = []
    for i in s.split(' '):
        if i.count('!') != 1:
            if i.strip() != '':
                a.append(i)
                print(a)
    return (' ').join(a)


#true v.

#def remove(s):
#   return ' '.join(i for i in s.split() if i.count('!') is not 1)


print(remove(' Y  NSTI  TA!!EF IS H ZR '))
