# In this Kata, you will be given a string and two indexes. Your task is to reverse the portion of that string between those two indexes inclusive.
#
# solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
# solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
# Input will be lowercase and uppercase letters only.


def solve(st, a, b):
    if a != 0:
        return st[:a] + st[b:a-1:-1] + st[b+1:]
    else:
        return st[b::-1] + st[b+1:]


print(solve("abcefghijklmnopqrstuvwxyz", 0, 20))

#
# def solve(st,a,b):
#     return st[:a]+st[a:b+1][::-1]+ st[b+1:]