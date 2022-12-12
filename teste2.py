from itertools import count

c1 = count()

for i in range(10):
    next(c1)
    print(c1)
