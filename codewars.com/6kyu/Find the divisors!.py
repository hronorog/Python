'''
Create a function named divisors that takes an integer and returns an array with all of the integer's divisors
(except for 1 and the number itself). If the number is prime return the string '(integer) is prime'

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''


def divisors(integer):
    mass = []
    for i in range(1, integer):
        if integer % i == 0:
            mass.append(i)
    if len(mass) > 1:
        return mass[1:]
    else:
        return "{} is prime".format(integer)


print(divisors(13))
print(divisors(15))


'''
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
'''