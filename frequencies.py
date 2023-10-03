"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        if (x in frequencies):
            frequencies[x] +=1
        else:
            frequencies[x] = 1
    print(frequencies)


items = ['a', 'a', 'b', 'b', 'b', 'c']
frequencies(items)

#cannout make str = int
items = [100, 'Hello', '100', '100', 100]
frequencies(items)
