# In this Kata, you will be given a string and your task is to determine if that string can be a palindrome if we rotate one or more characters to the left.
#
# solve("4455") = true, because after 1 rotation, we get "5445" which is a palindrome
# solve("zazcbaabc") = true, because after 3 rotations, we get "abczazcba", a palindrome


def solve(st):

    for i in range(len(st)):
        rt = st[-1]+st[:-1]
        if rt == rt[::-1]:
            return True
        else:
            st = rt
    return False


print(solve('4455'))

#
# def solve(s):
#     return any(s[i+1:] + s[:i+1] == s[i::-1] + s[:i:-1] for i in range(len(s)))
#
# q,solve=lambda p:p==p[::-1],lambda s:any(q(s[x:]+s[:x])for x in range(len(s)))