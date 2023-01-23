import time
import os
import requests
from requests import get
import pandas as pd
import json
from dotenv import load_dotenv
import streamlit as st

### 
# Import Azure KV secrets
###

st.set_page_config(layout="wide")

st.sidebar.header("Pages")
page_choices = ['Fireblocks WL','Exchanges WL', 'Ledger WL']
pages = st.sidebar.selectbox("Choose a Page", page_choices)
if pages == "Fireblocks WL":
    st.title("Fireblocks Whitelisted Wallets")
    github_path = ("addresses/fireblocks_whitelisted_wallets.csv")
    # Read the data frame from a CSV file
    df = pd.read_csv(r'C:\Users\arielma\Desktop\projects\WLSite\addresses\fireblocks_whitelisted_wallets.csv')

    del df["Balance"]
    del df["Address Type"]

    #df = pd.delete(filename)("Address Type","Balance")
    df = df[~df.isin(["wintermute"]).any(axis=1)]
    df = df[~df.isin(["LMAX"]).any(axis=1)]
    df = df[~df.isin(["Genesis"]).any(axis=1)]
    df = df[~df.isin(["Bittrex"]).any(axis=1)]
    df = df[~df.isin(["A-book Legacy"]).any(axis=1)]
    df = df[~df.isin(["B2C2"]).any(axis=1)]
    df = df[~df.isin(["Cumberland"]).any(axis=1)]
    df = df[~df.isin(["Jane Street Trading"]).any(axis=1)]



    st.dataframe(df,width=2000)
    
    
if pages == "Exchanges WL":
   
    st.title("Exchanges Whitelisted Wallets")
    # Load data into a dataframe
    df_exchange = pd.read_csv((r'C:\Users\arielma\Desktop\projects\WLSite\addresses\fireblocks_whitelisted_wallets.csv'))
    del df_exchange["Balance"]
    del df_exchange["Address Type"]
    # Create a boolean mask indicating which rows contain the values "binance" or "coinbase"
    mask = df_exchange['Wallet Name'].str.contains('binance|coinbase|kraken|Binance BVI|coinbase bvi|kraken bvi', case=False)

    # Use the mask to select only the rows that contain the values "binance" or "coinbase"
    df_filtered = df_exchange.loc[mask]
    st.dataframe(df_filtered,width=2000)
    

