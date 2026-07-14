from __future__ import annotations

import streamlit as st


def apply_filters(df):
    """
    Apply global filters and return filtered dataframe.
    """

    # ---------- Year ----------

    years = sorted(
        df["year"].dropna().astype(int).unique().tolist()
    )

    selected_year = st.sidebar.selectbox(
        "Year",
        ["All"] + years,
        key="selected_year"
    )

    # ---------- City ----------

    cities = sorted(
        df["city"].dropna().unique().tolist()
    )

    selected_city = st.sidebar.selectbox(
        "City",
        ["All"] + cities,
        key="selected_city"
    )

    filtered_df = df.copy()

    if selected_year != "All":

        filtered_df = filtered_df[
            filtered_df["year"] == selected_year
        ]

    if selected_city != "All":

        filtered_df = filtered_df[
            filtered_df["city"] == selected_city
        ]

    st.session_state.filtered_df = filtered_df

    return filtered_df


def startup_options(filtered_df):
    """
    Startup list after applying global filters.
    """

    if filtered_df.empty:
        return []

    return sorted(
        filtered_df["startup"]
        .dropna()
        .unique()
        .tolist()
    )


def investor_options(filtered_df):
    """
    Investor list after applying global filters.
    """

    if filtered_df.empty:
        return []

    investors = set()

    for row in filtered_df["investors"]:

        for investor in str(row).split(","):

            investor = investor.strip()

            if investor:
                investors.add(investor)

    return sorted(investors)