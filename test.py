from alg import *
import random

for n in range(100):
    i = [random.randrange(1000) for _ in range(n+1)]
    i.sort()
    goal = random.randrange(1000)
    r = goal in i
    mr, _ = binary_search(goal, i)
    assert r is mr

