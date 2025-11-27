import pandas as pd
import numpy as np

np.random.seed(42)

n_students = 50

studytime = np.linspace(1, 10, n_students)

noise = np.random.normal(0, 2, n_students)
score = 5 * studytime + 50 + noise

data = pd.DataFrame({
    'studytime': studytime,
    'score': score
})

data.to_csv('data.csv', index=False)

print("data.csv created with 50 students")
