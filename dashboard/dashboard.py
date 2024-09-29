import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

def distribution_of_interests(df):
    st.header("DISTRIBUTION OF PEOPLE'S INTEREST")
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    fig = plt.figure()
    sns.countplot(df["Interest"], order=df["Interest"].value_counts().index, palette=colors)
    st.pyplot(fig)

def home(df):
    st.header("DISTRIBUTION OF 16 PERSONALITIES 👀")
    
    with st.container():
        total_male = len(df[df["Gender"] == "Male"])
        total_female = len(df[df["Gender"] == "Female"])    
    
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(f"Total Data: {df.shape[0]}")

        with col2:
            st.subheader(f"Total Male\t: {total_male}")
            st.subheader(f"Total Female\t: {total_female}")
    
    fig = plt.figure()
    sns.barplot(data=df.groupby(["Personality", "Gender"])["Gender"].count().reset_index(name="Count").sort_values(by="Count", ascending=False), 
                  y="Count", 
                  x="Personality", 
                  hue="Gender",
                  palette=["#72BCD4", "#D3D3D3"])
    
    plt.xticks(rotation=45)
    st.pyplot(fig)

def main():
    df = pd.read_csv("https://raw.githubusercontent.com/hng011/people-personality-analysis/refs/heads/main/people_personality_types.csv")
    options = ["Home", "Distribution of Interests"]

    with st.sidebar:
        try:
            selected = option_menu(menu_title="Dashboard Menu",
                                   options=options,
                                   default_index=0)

        except:
            st.write("streamlit_option_menu was not found")
            st.write("Try to install the module using the following command")
            st.write("`pip install streamlit-option-menu`")

    if selected == options[0]:
        home(df)

    if selected == options[1]:
        distribution_of_interests(df)

if __name__ == "__main__":
    main()
