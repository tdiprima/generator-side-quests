# Demonstrates the difference between loading all data into memory
# vs. using a generator for processing lines from a large file efficiently.


def process_line(line):
    # Example processing: strip and upper case the line
    return line.strip().upper()


def gen_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield process_line(line)


# Usage
for item in gen_lines("../data/bigfile.csv"):
    print(item)

# Uncomment the following code to see the memory-intensive approach
# def load_all_lines(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
#     return [process_line(line) for line in lines]
# data = load_all_lines('bigfile.csv')
