import random
import numpy as np
import time
import math
import pandas as pd

def compute_eoc(errors, N_values):
    """
    Compute the estimated order of convergence (EOC) from successive error values.

    This function calculates the EOC using the formula:
        EOC = log(errors[i-1] / errors[i]) / log(N_values[i] / N_values[i-1])
    for i = 1, 2, ..., len(errors)-1. The first element of the returned list is set
    to infinity since the convergence order is undefined for the initial error value.

    Args:
        errors (list or array-like): A sequence of error values corresponding to 
            different levels of refinement.
        N_values (list or array-like): A sequence of parameter values (e.g., number 
            of elements or grid resolution) associated with each error value. It is 
            assumed that N_values[i] relates to errors[i].

    Returns:
        list: A list of EOC values where the first value is np.inf and subsequent 
            values represent the computed order of convergence between successive 
            error measurements.
    """
    eocs = [np.inf]  # First entry is undefined (or inf)
    for i in range(1, len(errors)):
        e = np.log(errors[i-1] / errors[i])
        h = np.log(N_values[i] / N_values[i-1])
        eocs.append(e / h)
    return eocs

def insertion_sort(A, n):
    c = 0
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>-1 and A[j]>key:
            A[j+1] = A[j]
            j -= 1
            c += 1
        A[j+1] = key
        c += 1
    return A, c

ns = [1000, 2000, 4000, 8000, 16000]
cs = []
for n in ns:
    arr = [random.randint(0, 100000) for _ in range(n)]
    _, c = insertion_sort(arr, n)
    cs.append(c)
eocs = compute_eoc(cs, ns)
df = pd.DataFrame({'n': ns, 'Error': cs, 'EOC': eocs})
print(df)