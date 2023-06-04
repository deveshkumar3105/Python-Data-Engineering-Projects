# Module Created for DataSummarization.
import pandas as pd

# Count the number of records in DataFrame
def count(df):
    recordCount = df.count()
    return recordCount

# Mean of a column in DataFrame Column
def mean(col,df):
    meanDF = df[col].mean(numeric_only=True)
    return meanDF

# Standard Deviation in DataFrame Column
def stdDev(col,df):
    std = df[col].std()
    return std

# Maximum of a column in DataFrame
def max(col,df):
    max = df[col].max()
    return max

# Minimum of a column in DataFrame
def min(col,df):
    min = df[col].min()
    return min

