"""These are helper functions""" 
import pandas as pd
import numpy as np

class CleaningDatabase(pd.DataFrame):
        def null_count(self):
            df2 = self.isnull().sum()
            dfsum = df2.sum()
            return dfsum



def list_2_series(list,df):
    df2 = df[pd.Series(list)]
    return df2