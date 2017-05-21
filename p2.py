# make random CODE

import random
import string


def make_code():
    salt = ''.join(random.sample(string.ascii_uppercase+string.digits, 20))
    return salt

for i in range(200):
    i += 1
    data = 'CODE'+str(i)+': '+make_code()+'\n'
    print data
