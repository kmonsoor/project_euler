""" 
# Detailed understandable edition
def is_pandigital(n):
    return len(str(n))==9 and not '123456789'[:9].strip(str(n))

result = 0
for i in xrange(9,9999): # in hope that the initial will be within 9999
    s = ""
    possible = True
    for j in range(1,6):
        s += str(i*j)
        if len(s) > 9 or '0' in s:
            break
        if len(s) == 9 and is_pandigital(s):
            if int(s) > result:
                    result = int(s)
            else:
                pass
        else:
            continue
    if possible == False:
        continue
print result


# short pro edition
result = 918273645
for i in xrange(9000,9999):
    s = ''
    for j in range(1,3):
        s += str(i*j)
        if len(s) > 9 or ('0' in s): break
        elif len(s) < 9: continue
        if (not '123456789'.strip(s)) and (int(s) > result):
            result = int(s)
print result
"""

# one-liner
max([int(str(i)+str(2*i)) for i in xrange(9000,9999) if (int(str(i)+str(2*i)) > 918273645) and not ('123456789'.strip(str(i)+str(2*i)))])
