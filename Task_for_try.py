from copy import copy
import random
import string
s= string.ascii_lowercase+string.ascii_uppercase+string.digits
a = 'Ivan'+''.join(random.sample(s,10))
d = copy(a)
