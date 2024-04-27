import random

def even_or_odd():
        n = random.randrange(1,101)
        if n % 2 == 0:
            print(n, "is an even number.")
        else:
            print(n, "is an odd number.")

for i in range(10):
    even_or_odd()
