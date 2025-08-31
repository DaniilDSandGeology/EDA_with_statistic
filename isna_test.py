import pandas as pd


def isna_test(df):
    """test of null

    Args:
        df (_type_): data frame
    """
    col_index = dict()
    for col in df:
        if df[col].isna().sum() > 0:
            col_index[col] = df[col].isna().sum()
        else:
            pass
    if len(col_index) == 0:
        print('пропусков нет')
    else:
        return (pd.Series(col_index))
