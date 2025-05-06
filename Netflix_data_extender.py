import pandas as pd
import random
import os

# File path
input_path = r"C:\Users\Hp\Downloads\1910_m4_assign_dataset_v1_1g7_h5gs6vm (2)\1910_m4_assign_dataset_v1.0.xlsx"

# Load the correct sheet
df = pd.read_excel(input_path, sheet_name='titles')

# Print column names to confirm
print("✅ Loaded columns:", df.columns)

# Add demographic columns
genders = ['Male', 'Female', 'Mixed']
age_groups = ['13-17', '18-24', '25-34', '35-44', '45+']

df['Gender'] = df['title'].apply(lambda x: random.choice(genders))
df['Age Group'] = df['title'].apply(lambda x: random.choice(age_groups))
df['Viewers'] = df['title'].apply(lambda x: random.randint(100000, 2000000))

# Save to a specific location
output_path = r"C:\Users\Hp\Documents\netflix_extended_dataset.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Dataset extended and saved to:\n{output_path}")
