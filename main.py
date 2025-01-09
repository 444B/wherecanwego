# data comes from https://github.com/ilyankou/passport-index-dataset/blob/master/passport-index-matrix-iso2.csv


import json

import pandas as pd
import streamlit as st

# read json data
with open("country_2_iso.json", "r") as f:
    json_data = json.load(f)

all_visas_statuses = [
    "visa free",
    "visa on arrival",
    "e-visa",
    "visa required",
    "no admission",
]
all_duration_lengths = [
    "7",
    "10",
    "14",
    "15",
    "21",
    "28",
    "30",
    "31",
    "42",
    "45",
    "60",
    "90",
    "120",
    "150",
    "180",
    "240",
    "360",
]


# allows the user to select their passports
def select_passport_names() -> list:
    list_of_country_names = st.multiselect(
        "Issuing Country:", json_data.values(), placeholder="Select passports"
    )
    return list_of_country_names


# converts a list of passport cointries to a list of their respective 2 letter ISO codes
def select_passport_isos(passport_names: list) -> list:
    list_of_isos = []
    for passport in passport_names:
        for iso, country in json_data.items():
            if country == passport:
                list_of_isos.append(iso)
    return list_of_isos


# Takes in a list of all the possible visa types and lets the user select their choices
def select_acceptable_visas(all_visas_statuses: list) -> list:

    acceptable_visas_statuses = st.multiselect(
        "Acceptable Visas", all_visas_statuses, "visa free"
    )
    return acceptable_visas_statuses


# Takes in a list of all the possible dates and lets the user select their choices
def select_acceptable_dates(all_visas_statuses: list) -> list:
    acceptable_visas_statuses = st.select_slider(
        "Acceptable Duration", all_visas_statuses, value=("30", "90")
    )
    return acceptable_visas_statuses


def main() -> None:
    st.header("Where can we go ✈️🎫")

    st.write(
        "See which countries you can all plan a trip to without worrying about visas!"
    )

    # Create a section for selecting passport and a button to add more
    with st.container(border=True):

        col1, col2 = st.columns([1, 1], border=True)

        # Select Passports
        with col1:
            st.write("Passports")
            passport_names = select_passport_names()
            passport_isos = select_passport_isos(passport_names)

        # Select acceptable Visas / lengths of stay
        with col2:
            st.write("Visas")
            acceptable_visas = select_acceptable_visas(all_visas_statuses)
            st.write("OR")
            acceptable_length = select_acceptable_dates(all_duration_lengths)

    # Section to display the data
    with st.expander("Results", expanded=True):
        st.write(f"You have selected {passport_names}")

        # this shows the entire data we have on which countries accept visas from each other
        visa_df = pd.read_csv("visa_data.csv")

        # this shows the info for the countries selected
        filtered_df = visa_df[visa_df["Passport"].isin(passport_isos)]
        filtered_df

        # TODO We need to adjust filtered_df even further to only show countries
        # that are in in the acceptable_visas list

        # TODO Add error handling for countries for which there is no data
        # Examples: Aland Islands, Antarctica, American Samoa


if __name__ == "__main__":
    main()
