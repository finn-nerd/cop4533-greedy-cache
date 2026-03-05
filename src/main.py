import ID, math
from data_helpers import generate_input_file
from eviction_policies import FIFO, LRU, OPTFF

# Main program
def main():
    # Get the input file path from the user
    file_path = input("Enter the input file path: ")

    # Try to open the file at the file path
    try:
        with open(file_path, 'r') as f:
            # Splits line into pieces using whitespace and converts the strings into ints
            k, m = map(int, f.readline().split())
            ids = list(map(int, f.readline().split()))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Validate k
    if k < 1:
        print("Error: The cache capacity is too small.")
        return
    
    # Validate that the size of ids is m
    if len(ids) != m:
        print("Error: The sequence of integer IDs is not the same size as 'm'.")
        return
    
    # Initialize our caches
    cache1 = []
    cache2 = []
    cache3 = []

    # Get the hits/misses of utilizing each eviction policy
    hits_FIFO, misses_FIFO = addToCache(k, m, ids, cache1, 1)
    hits_LRU, misses_LRU = addToCache(k, m, ids, cache2, 2)
    hits_OPTFF, misses_OPTFF = addToCache(k, m, ids, cache3, 3)

    # Write the hits/misses into an output file
    o_file_path = input("Enter the output file path (optional): ")

    # Print result
    print(f"FIFO  : {misses_FIFO}")
    print(f"LRU   : {misses_LRU}")
    print(f"OPTFF : {misses_OPTFF}")

    # Write to output file
    try:
        with open(o_file_path, 'w') as f:
            f.write(f"FIFO  : {misses_FIFO}\n")
            f.write(f"LRU   : {misses_LRU}\n")
            f.write(f"OPTFF : {misses_OPTFF}\n")
        print("Wrote output to file.")
    except FileNotFoundError:
        print("Output file not found, exiting.")

# Adds ids to cache depending on eviction policy
def addToCache(k, m, ids, cache, policy):
    # Record number of hits/misses for the policy
    hits = 0
    misses = 0

    i = 0 # index
    time = 0 # time

    # Add each id to our cache
    while i < m:
        newID = ID.ID(ids[i])

        # See if id is in cache already
        if newID in cache:
            hits += 1

            # find the id in cache already and update its access time
            cache[cache.index(newID)].setLastAccessed(time)
        else:
            misses += 1

            newID.setEnteredCache(time)
            newID.setLastAccessed(time)

            # If cache isn't full, add id to cache
            if len(cache) < k:
                cache.append(newID)
            else:
                # Determine which eviction policy to use
                if policy == 1:
                    FIFO(cache, newID)
                elif policy == 2:
                    LRU(cache, newID)
                elif policy == 3:
                    OPTFF(cache, newID)

        # Update ID's next access
        found = False
        for j in range(i + 1, m):
            if ids[j] == newID.personalID:
                cache[cache.index(newID)].setNextRequest(j)
                found = True
                break
        if not found:
            cache[cache.index(newID)].setNextRequest(math.inf)

        time += 1
        i += 1

    return hits, misses
                

if __name__ == "__main__":
    main()
