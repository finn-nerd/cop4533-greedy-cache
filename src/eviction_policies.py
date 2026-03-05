import ID

# FIFO: Evict the item that has been in the cache the longest.
def FIFO(cache, newID: ID):
    # Find oldest cache item
    firstIn: ID = None
    for id in cache:
        if (firstIn is None) or (id.enteredCache < firstIn.enteredCache):
            firstIn = id
    # Evict first-in, enter newID
    cache[cache.index(firstIn)] = newID
    

# LRU: Evict the item whose most recent access time is the oldest.
def LRU(cache, newID: ID):
    # Find least recently used item
    leastUsed: ID = None
    for id in cache:
        if (leastUsed is None) or (id.lastAccessed < leastUsed.lastAccessed):
            leastUsed = id
    # Evict least-used, enter newID
    cache[cache.index(leastUsed)] = newID

# OPTFF: Among items currently in the cache, evict the one whose next request occurs farthest in the future (or never occurs again).
def OPTFF(cache, newID: ID):
    # Find item needed farthest in future
    farthest: ID = None
    for id in cache:
        if (farthest is None) or (id.nextRequest > farthest.nextRequest):
            farthest = id
    # Evict farthest-used, enter newID
    cache[cache.index(farthest)] = newID