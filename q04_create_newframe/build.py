import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q03_remove_wordcount.build import q03_remove_wordcount
path = 'data/episource.txt'




def q04_create_newframe(path):
    "write your solution here"
    df_above_5 = q03_remove_wordcount(path)
    condition = (df_above_5['words'].str.len() > 5) & (df_above_5['count'] > 10)

    # Apply the condition on the existing df and select the required rows
    conditional_df = df_above_5.loc[condition]
    return conditional_df
