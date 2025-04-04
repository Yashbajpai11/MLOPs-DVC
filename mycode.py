import pandas as pd
import os

data = {
    'name': ['yash', 'varsha', 'aishwarya'],
    'Age': [22, 23, 22],  # Age column ki length sabhi rows ke liye match honi chahiye
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

new_row_loc = {'name':'gf1','Age':24,'City':'city1'}
df.loc[len(df.index)] = new_row_loc

new_row_loc2 = {'name':'gf2','Age':24,'City':'city2'}
df.loc[len(df.index)] = new_row_loc2



# Directory banana
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# CSV file ka path
file_path = os.path.join(data_dir, 'sample_data.csv')

# CSV file save karna
df.to_csv(file_path, index=False)

print(f'CSV file saved to {file_path}')

