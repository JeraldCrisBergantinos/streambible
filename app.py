# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA Pkgs
import pandas as pd
import neattext.functions as nfx
import random

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

from utils import HTML_RANDOM_TEMPLATE

def main():
    st.title("StreamBible")
    menu = ["Home", "MultiVerse", "About"]

    df = load_bible("data/KJV_Bible.csv")

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Single Verse Search")

        #st.dataframe(df)
        book_list = df["book"].unique().tolist()
        book_name = st.sidebar.selectbox("Book", book_list)
        chapter = st.sidebar.number_input("Chapter", 1)
        verse = st.sidebar.number_input("Verse", 1)
        bible_df = df[df["book"] == book_name]
        #st.dataframe(bible_df)

        # Layout
        c1, c2 = st.columns([2,1])

        # Single Verse Layout
        with c1:
            try:
                selected_passage = bible_df[(bible_df["chapter"] == chapter) & (bible_df["verse"] == verse)]
                #st.write(selected_passage)
                passage_details = "{} Chapter::{} Verse::{}".format(book_name, chapter, verse)
                st.info(passage_details)
                passage = "{}".format(selected_passage["text"].values[0])
                st.write(passage)

            except:
                st.warning("Book out of range")

        with c2:
            #st.success("Verse of the Day")
            chapter_list = range(10)
            verse_list = range(20)
            ch_choice = random.choice(chapter_list)
            vs_choice = random.choice(verse_list)
            random_book_name = random.choice(book_list)

            #st.write("Book: {}, Chapter: {}, Verse: {}".format(random_book_name, ch_choice, vs_choice))
            random_bible_df = df[df["book"] == random_book_name]
            random_selected_passage = random_bible_df[(random_bible_df["chapter"] == ch_choice) & (random_bible_df["verse"] == vs_choice)]

            try:
                random_selected_passage = random_bible_df[(random_bible_df["chapter"] == ch_choice) & (random_bible_df["verse"] == vs_choice)]
                mytext = random_selected_passage["text"].values[0]
            except:
                mytext = random_bible_df[(random_bible_df["chapter"] == 1) & (random_bible_df["verse"] == 1)]["text"].values[0]

            stc.html(HTML_RANDOM_TEMPLATE.format(mytext), height=300)

        # Search Topic/Term
        search_term = st.text_input("Term/Topic")
        with st.expander("View Results"):
            retrieved_df = df[df["text"].str.contains(search_term)]
            st.dataframe(retrieved_df[["book", "chapter", "verse", "text"]])

    elif choice == "MultiVerse":
        st.subheader("MultiVerse Retrieval")

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()