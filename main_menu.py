from inspect import getmembers, isfunction
from random import shuffle

from visualiser import visualise

import sorting


N = 30 #int(input("Enter number of elements: "))     # number of elements
array = [i + 1 for i in range(N)]   # array to sort
shuffle(array)  #shuffle array

algorithm_names = [o[0] for o in getmembers(sorting) if isfunction(o[1])]
algorithms = [o[1] for o in getmembers(sorting) if isfunction(o[1])]


print("Welcome to Algorithm Visualiser")
for i, algorithm in enumerate(algorithm_names):
    print(f"{i+1}. {algorithm}")

algorithm = int(input("Select which algorithm to visualise: "))

print(f"You selected {algorithm_names[algorithm-1]}")

title = algorithm_names[algorithm-1]
algorithm = algorithms[algorithm-1](array)

visualise(algorithm, array)