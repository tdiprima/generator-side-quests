# Demonstrates list comprehension vs. generator expression for
# generating squares without loading everything into memory.

# List comprehension (loads all into memory)
squares_list = [x * x for x in range(1000000)]

# Generator expression (lazy evaluation)
squares_gen = (x * x for x in range(1000000))

# Usage: Consume a few from generator
for i, square in enumerate(squares_gen):
    if i >= 5:
        break
    print(square)
