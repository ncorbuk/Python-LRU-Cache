
import time

#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)

class Node:
    #Nodes - (n)=(n)=(n)=(n)
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    cache_limit = 3

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def __call__(self, *args, **kwargs):
        #If in cache, pull results
        if args in self.cache:
            self.llist(args)

            return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'

        #If cache-limit reached - Remove LRU from node link list and dict - cache.
        if len(self.cache) > self.cache_limit:
            n = self.head.next
            self._remove(n)
            del self.cache[n.key]



        #Compute and cache and node - if not in cache
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        return f'{result}\nCache: {self.cache}'

    #Remove from double linked-list - Node.
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
 
    #Add to double linked-list - Node.
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def llist(self, args):
        current = self.head
        while current != (0,0):
            if current.key == args :
                node = current
                self._remove(node)
                self._add(node)
                del self.cache[node.key]  #Debuging / See how cache order changes keeping most recent at top(tail) and least at bottom(head)
                self.cache[node.key] = node.val #Debuging / See how cache order changes keeping most recent at top(tail) and least at bottom(head)
                break
            else:
                current = current.next



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

#Copyright (c) 2018 - Nathan Corbin - @ncorbuk(Twitter)
