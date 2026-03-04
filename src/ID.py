import math

class ID:
    # Initialize properties of each ID
    def __init__(self, personalID):
        self.personalID = personalID
        self.enteredCache = math.inf
        self.lastAccessed = math.inf
        self.nextRequest = 0

    # Set when the ID entered the cache (FIFO)
    def setEnteredCache(self, enteredCache):
        self.enteredCache = enteredCache

    # Set when the ID was last accessed (LRU)
    def setLastAccessed(self, lastAccessed):
        self.lastAccessed = lastAccessed

    # Set when next request of this ID is (OPTFF)
    def setNextRequest(self, nextRequest):
        self.nextRequest = nextRequest
