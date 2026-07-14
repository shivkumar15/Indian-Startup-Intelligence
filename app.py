from __future__ import annotations

import streamlit as st

from config import APP_NAME
from utils.loader import DataLoader
from core import (
    initialize_state,
    build_sidebar,
    route_page,
)


st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_state()

dataframe = DataLoader.load()

sidebar = build_sidebar(dataframe)

route_page(
    page=sidebar["page"],
    filtered_df=sidebar["filtered_df"],
    selected_year=sidebar["selected_year"],
    selected_city=sidebar["selected_city"],
    selected_startup=sidebar["selected_startup"],
    selected_investor=sidebar["selected_investor"],
)