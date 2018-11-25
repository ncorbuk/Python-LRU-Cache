# Python-LRU-Cache
Python implementation of Least Recently Used Cache (LRU Cache) using dict and linked list.
*Simple, Elegant, Lru Cache wrapper...*

## Description
This LRUCache code, will create a cache(dict) and a linked list per each *instance* eg. per each function the wrapper class is used on
like so..

```
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
print(ex_func_01(4)) # Cache: {(5,): 25, (4,): 16} <-- 4 is moved from the bottom to the top of cache
print(ex_func_01(6)) # Cache: {(5,): 25, (4,): 16, (6,): 36}

print(f'\nFunction: ex_func_02')
print(ex_func_02(7)) # Cache: {(7,): 49}
print(ex_func_02(8)) # Cache: {(7,): 49, (8,): 64}
print(ex_func_02(4)) # Cache: {(7,): 49, (8,): 64, (4,): 16}
print(ex_func_02(7)) # Cache: {(8,): 64, (4,): 16, (7,): 49} <-- 7 is moved from bottom the to top of cache
```

This cache will remove the least used(at the bottom) when the cache limit is reached or in this case is one over the cache limit, and will move cached results to the top if are called again and already in cache, or add new results to the top if not... keeping most recently used at the top for further use.

Simple system.

## Testing
To test it and see what i mean run the code, **python LRUCache.py** in terminal.

## Built With

* **Python 3.6.5** - [https://www.python.org/](https://www.python.org/)

## Authors

* **Nathan Corbin** - *Github*: [ncorbuk](https://github.com/ncorbuk) - *Twitter*: [@ncorbuk](https://twitter.com/ncorbuk)
