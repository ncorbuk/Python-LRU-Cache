
import time
from LRUCache import LRUCache

LRUCache.testing = 1 # DEFAULTS to 0. Setting to 1 will be able to see cache list and how it changes and moves items up and off list
                     # and inner workings of program and for debugging...

LRUCache.cache_limit = 3 # DEFAULTS to 3. But can change like so to any number that is needed.
# Cache_limt > 3 ... then it will remove bottom cached result. It allows for 1 extra result over the set cache limit.

@LRUCache
def ex_func_01(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n


@LRUCache
def ex_func_02(n):
    print(f'Computing...{n}x{n}')
    time.sleep(1)
    return n*n

print(f'\nFunction: ex_func_01')
print(ex_func_01(4)) # Cache: {(4,): 16}
print(ex_func_01(5)) # Cache: {(4,): 16, (5,): 25}
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16}
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}

print(f'\nFunction: ex_func_02')
print(ex_func_02(7)) # Cache: {(7,): 49}
print(ex_func_02(8)) # Cache: {(7,): 49, (8,): 64}
print(ex_func_02(4)) # Cache: {(7,): 49, (8,): 64, (4,): 16}
print(ex_func_02(7)) # Cache: {(8,): 64, (4,): 16, (7,): 49}
