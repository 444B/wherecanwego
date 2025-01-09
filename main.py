# data comes from https://github.com/ilyankou/passport-index-dataset/blob/master/passport-index-matrix-iso2.csv


import json

import pandas as pd
import streamlit as st

# read json data
with open("country_2_iso.json", "r") as f:
    json_data = json.load(f)

# list of acceptable visa statuses
acceptable_visas_statuses = [
    "visa free",
    "visa on arrival",
    "e-visa",
    "30",
    "90",
    "180",
]
# TODO make this ^ a selectable list so that users can decide for themselves what is acceptable


def select_passport_name():
    list_of_country_names = st.multiselect("Issuing Country:", json_data.values())

    return list_of_country_names


def select_passport_isos(passport_names):
    isos = []
    for passport in passport_names:
        for iso, country in json_data.items():
            if country == passport:
                isos.append(iso)
    return isos


def main():
    st.header("Where can we go bro")

    # Create a section for selecting passport and a button to add more
    with st.container():
        col1, col2 = st.columns([8, 1], border=True)

        # Select Passport
        with col1:
            passport_names: list = select_passport_name()
            passport_isos: list = select_passport_isos(passport_names)

        # Button to add another passport
        with col2:
            if st.button("\+"):
                pass  # TODO

    # Section to display the data
    with st.expander("Results", expanded=True):
        st.write(f"You have selected {passport_names}")

        # this shows the entire data we have on which countries accept visas from each other
        visa_df = pd.read_csv("visa_data.csv")

        # this shows the info for the countries selected
        filtered_df = visa_df[visa_df["Passport"].isin(passport_isos)]
        filtered_df

        # TODO We need to adjust filtered_df even further to only show countries
        # that are in acceptable_visa_status[]

        # TODO Add error handling for countries for which there is no data
        # Examples: Aland Islands, Antarctica, American Samoa


if __name__ == "__main__":
    main()
