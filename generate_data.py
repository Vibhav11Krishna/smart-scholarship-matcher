import pandas as pd
import numpy as np

# Generate a lightweight synthetic or structured dataset mimicking your exact columns
np.random.seed(42)
n_rows = 5000

data = {
    'Name': [f'Scholarship Scheme {i}' for i in range(1, n_rows + 1)],
    'Education Qualification': np.random.choice(['Undergraduate', 'Postgraduate', 'Doctorate', 'High School'], n_rows),
    'Gender': np.random.choice(['All', 'Female', 'Male'], n_rows),
    'Community': np.random.choice(['General', 'OBC', 'SC', 'ST'], n_rows),
    'Religion': np.random.choice(['Hindu', 'Muslim', 'Sikh', 'Christian'], n_rows),
    'Exservice-men': np.random.choice(['Yes', 'No'], n_rows),
    'Disability': np.random.choice(['Yes', 'No'], n_rows),
    'Sports': np.random.choice(['Yes', 'No'], n_rows),
    'Annual-Percentage': np.random.uniform(50.0, 99.9, n_rows).round(2),
    'Income': np.random.choice(['Low', 'Medium', 'High'], n_rows),
    'India': np.random.choice(['Yes'], n_rows),
    'Outcome': np.random.choice([0, 1], n_rows, p=[0.6, 0.4])
}

df = pd.DataFrame(data)

# Save as a lightweight CSV file (less than 500KB)
df.to_csv('dataset_combined.csv', index=False)
print("Lightweight dataset created successfully!")