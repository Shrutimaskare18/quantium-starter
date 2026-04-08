import pandas as pd
import glob

# Step 1 — teenon CSV files padhna
files = glob.glob('data/*.csv')
df_list = []

for file in files:
    df_list.append(pd.read_csv(file))

# Step 2 — combine karo
df = pd.concat(df_list, ignore_index=True)

# Step 3 — sirf Pink Morsel filter karo
df = df[df['product'] == 'pink morsel']

# Step 4 — sales column banao (quantity x price)
df['sales'] = df['quantity'] * df['price']

# Step 5 — sirf 3 columns rakho
df = df[['sales', 'date', 'region']]

# Step 6 — output file save karo
df.to_csv('output.csv', index=False)

print("Done! output.csv ready hai")




