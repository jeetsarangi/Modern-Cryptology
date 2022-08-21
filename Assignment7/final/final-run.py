

# using itertools to import combinations_with_replacement for creating combinations.
from itertools import combinations_with_replacement
L  = [i for i in range(ord('f'),ord('u')+1)]
a = combinations_with_replacement (L, 23)

# the function will return modulo power 
def fun(num,p,mod):
    return pow(num,p,mod)
# mapper fucntion will apply the fun fucntion on the given sequence of numbers.
def mapper(a_list,p):
    res = [fun(i,p,127) for i in a_list]
    return res
# given
hashcode = [23,5,47,55 ,19, 32, 115, 112, 56, 75, 72, 67, 74, 92, 39, 37, 22, 69, 107, 91, 89, 59, 66, 11, 41, 48, 28, 30, 33, 29, 3, 66]
# hashcode = [23,5,47]
# the loop will print the answer
for i in a:
    flag = True
    for idx,j in enumerate(hashcode):
        if(idx == 0):
            continue
        flag = flag and (sum(mapper(i,idx))%127 == j)
        if not flag:
            break
    if flag:
        print(i)



