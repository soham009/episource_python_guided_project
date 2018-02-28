import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q02_create_dataframe.build import q02_create_dataframe
path = 'data/episource.txt'


def q03_remove_wordcount(path):
    "write your solution here"
    df = q02_create_dataframe(path)

    # Create the required condition
    df_above_5 = df[df['count'] >= 5]
    return df_above_5
