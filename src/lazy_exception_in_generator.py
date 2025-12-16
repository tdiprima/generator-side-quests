# Demonstrates how exceptions in generators are raised only during iteration.


def faulty_gen():
    for i in range(5):
        if i == 3:
            raise ValueError("Something went wrong!")
        yield i


gen = faulty_gen()  # No error yet

try:
    for x in gen:
        print(x)  # Prints 0-2, then raises error at 3
except ValueError as e:
    print(f"Caught error: {e}")
