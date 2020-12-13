from random import shuffle
from matplotlib import pyplot as plt
from matplotlib import animation as anim

from inspect import getmembers, isfunction

import sorting


N = 100     # number of elements
array = [i + 1 for i in range(N)]   # array to sort
shuffle(array)  #shuffle array



algorithm_names = [o[0] for o in getmembers(sorting) if isfunction(o[1])]
algorithms = [getattr(sorting, algorithm_name) for algorithm_name in algorithm_names]


print("Welcome to Algorithm Visualiser")
for i, algorithm in enumerate(algorithm_names):
    print(f"{i+1}. {algorithm}")

algorithm = int(input("Select which algorithm to visualise: "))

print(f"You selected {algorithm_names[algorithm-1]}")

algorithm = algorithms[algorithm-1]

print(algorithm)