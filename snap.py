import streamlit as st
import pandas as pd


st.title('simple_test_site')

#Full Data Caching
url = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
@st.cache
def get_data() -> pd.DataFrame:
    return pd.read_csv(url, compression='gzip', sep='\t')
df = get_data()

