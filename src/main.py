import ID

def main():
    # Get the input file path from the user
    file_path = input("Enter the input file path.")

    # Try to open the file at the file path
    try:
        with open(file_path, 'r') as f:
            # Splits line into peices using whitespace and converts the strings into ints
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
    
    # Initialize our cache to size k
    cache = [None] * k

    i = 0

    # Add each id to our cache
    while i < m:
        newID = ID(ids[i])


    file.close()

if __name__ == "__main__":
    main()
