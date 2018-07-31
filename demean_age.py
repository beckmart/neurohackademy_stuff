import sys
import numpy as np
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t')

mean_age = sum(age)/len(age)

assert mean_age < 100
assert mean_age > 10 

mean_age = sum(age)/len(age)

np.savetxt("demeaned_age.txt", age-mean_age)

print("done!")