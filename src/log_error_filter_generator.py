# Demonstrates filtering error lines from a log file using a generator
# to avoid memory overload.


def process(line):
    # Example processing: add a prefix to the error line
    return f"Processed Error: {line.strip()}"


def error_lines(path):
    with open(path, "r") as f:
        for line in f:
            if "ERROR" in line:
                yield line


# Usage
for error in error_lines("../data/logs.txt"):
    print(process(error))
