"""
lambdata - A collection of Data Science helper functions.
"""

import pandas as pd
import numpy as np


"""
Convert all missing value in a specified column to the median.
"""
def missing_median(df, name):
  median = df[name].median()
  df[name] = df[name].fillna(median)


"""
Check a dataframe for nulls.
"""
def nulls_in_a_df(df, name):
  if df[name].isna().sum()>=0:
    print('DataFrame has null values')
  else:
    print('There are no nulls')
