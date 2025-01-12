import pandas as pd
import numpy as np
from pandas.tseries.offsets import DateOffset
from datetime import date
from components.tvdatafeed_lib import TvDatafeed

def df_book_iteration(df_book_var: pd.DataFrame, ativos_org_var = {}) -> dict:
    for _, row in df_book_var.iterrows():
        if not any (row['ativo'] in sublist for sublist in ativos_org_var):
            ativos_org_var[row['ativo']] = row['exchange']

    ativos_org_var['IBOV'] = 'BMFBOVESPA'
    return ativos_org_var

def historical_data_update(df_historical_var: pd.DataFrame, ativos_org_var = {}) -> pd.DataFrame:
    tv = TvDatafeed()
    for symb_dict in ativos_org_var.items():
        new_line = tv.get_hist(*symb_dict, n_bars=5000)[['symbol', 'close']].reset_index()
        df_historical_var = pd.concat([df_historical_var, new_line], ignore_index=True)
    
    return df_historical_var.drop_duplicates(ignore_index=True)