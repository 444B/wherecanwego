# data comes from https://github.com/ilyankou/passport-index-dataset/blob/master/passport-index-matrix-iso2.csv


import streamlit as st
import pandas as pd
import json

# load the countries to iso
with open('countries_2_iso.json', 'r') as f:
    json_data = json.load(f)

countries_dict = json_data

df = pd.DataFrame({'Country': json_data.values(), 'Key': json_data.keys()})


def add_passport():
    country = st.multiselect("Issuing Country:",countries_dict.values())
    return country




def main():
    st.header("Passport Compatible Matrix")

    with st.container():
        col1, col2 = st.columns([8, 1], border=True)
        
        with col1:
            passport = add_passport()

        with col2:
            if st.button("\+"):
                add_passport()

    

    with st.expander("Results",expanded=True):
        st.write(f"You have selected {passport}")

        data_df = pd.read_csv("country_data.csv")
        data_df



    df


def get_passport() -> str:
    return 



if __name__ == "__main__":
    main()
