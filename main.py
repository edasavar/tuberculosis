 # path to dataset
 # C:\\Users\\Eda\\.cache\\kagglehub\\datasets\\ankushpanday1\\tuberculosis-tb-predictiontop-75-countries\\versions\\1

# create notebook
# %% 
import pandas as pd
import matplotlib.pyplot as plt

# read data into dataframe
df = pd.read_csv("C:\\Users\\Eda\\.cache\\kagglehub\\datasets\\ankushpanday1\\tuberculosis-tb-predictiontop-75-countries\\versions\\1\\Tuberculosis_Dataset.csv")

country_df = df.sort_values(by=['Country'], ascending=False)
# %%
# preview data
# print(df)

# print("\n ---------- \n")

# investigating dataset


df_info = df.info()
print(df_info)

# number of numeric columns(! objects in df_info)

# number of object columns(= objects in df_info)

# find unique values in data
for i, col in enumerate(df.columns):
    print('-----------------------------------------------------------')
    print(f'{i+1}. {col}({df[col].nunique()}) : \n {df[col].unique()} ')
    
# other thoughts
# is there equal number of rows for each country? how many is that?

# key statistics
# population
# female vs male mortality rate for the various age groups
# TB related mortality rate corrolation with smoking 
# TB related mortality rate corrolation with alcohol
# TB related mortality rate/occurance corrolation with vaccination coverage
# screening coverage vs mortality rate
# Rural population percentage vs mortality rate