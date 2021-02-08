"""Lambdata - A collection of Data Science Helper Functions"""

import pandas
import numpy


def df_cleanser(df):
    """Cleans pd.DataFrame"""
    # TODO - Implement
    pass
def null_count(df):
    df2 = df.isnull().sum()
    dfsum = df2.sum()
    return dfsum()