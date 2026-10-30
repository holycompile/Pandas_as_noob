import pandas as pd 

df = pd.read_JSON('data.json') # search for some json file 

print(df.to_string())