import random

# Generate an input file based on parameters
def generate_input_file(file_path, k, m, minRange, maxRange):
    with open(file_path, 'w') as f:
        f.write(f"{k} {m}\n")
        for i in range(0, m):
            f.write(str(random.randint(minRange, maxRange)))
            f.write(" ")
