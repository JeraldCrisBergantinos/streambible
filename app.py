# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd
import neattext.functions as nfx

# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

# Utils
@st.cache
def load_bible(data):
    df = pd.read_csv(data)
    return df

def main():
    st.title("StreamBible")
    menu = ["Home", "MultiVerse", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Single Verse Search")

    elif choice == "MultiVerse":
        st.subheader("MultiVerse Retrieval")

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()