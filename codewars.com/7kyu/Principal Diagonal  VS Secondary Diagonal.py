# Principal Diagonal -- The principal diagonal in a matrix identifies those elements of the matrix running from north-west to south-east. An example of this diagonal :
# [1,0,0]
# [0,1,0]
# [0,0,1]
#
# elements of Principal Diagonal 1, 1, 1 .
#
# Secondary Diagonal -- the secondary diagonal of amatrix identifies those elements of the matrix running from north-east to south-west. An example of this diagonal :
#
# [0,0,1]
# [0,5,0]
# [2,0,0]
#
# elements of Seconrady Diagonal 1, 5, 2 .
#
# 3+8+2 > 0+8+0 => return 'Principal diagonal win!'
#
# Your task is to find which diagonal is larger (which a diagonal have bigger sum of their elements).
#
# If the primary diagonal is larger,--> return "Principal Diagonal win!".
#
# If the secondary diagonal is larger,--> return "Secondary Diagonal win!".
#
# if it's draw,--> return "Draw!".
#
# You will always receive matrices of the same dimension

def diagonal(matrix):
    sumP = sumS = 0
    for x, y in enumerate(matrix):
        sumP += y[x]
        sumS += y[-x-1]

    if sumP > sumS:
        return "Principal Diagonal win!"
    elif sumP < sumS:
        return "Secondary Diagonal win!"
    else:
        return "Draw!"

# def diagonal(matrix):
#     sp, ss = map(sum, zip(*((matrix[x][x], matrix[len(matrix)-1-x][x]) for x in range(len(matrix)))))
#     return "Draw!" if ss == sp else "{} Diagonal win!".format("Principal" if sp > ss else "Secondary")
#
# ---
#
# q,diagonal=lambda x:(x==0)*2+(x>0),lambda m:["Secondary Diagonal win!","Principal Diagonal win!",'Draw!'][q(sum(x[y]-x[::-1][y] for y,x in enumerate(m)))]