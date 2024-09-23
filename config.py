import os

import pandas as pd
import streamlit as st


CURRENT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
USER_DATA_PATH = f'{CURRENT_DIR_PATH}/storage/USER_DATA.csv'
USER_DATA = pd.read_csv(USER_DATA_PATH)

BEER_NAMES = USER_DATA[USER_DATA['BEER'].notnull()]['BEER'].sort_values(ascending=True).unique()
BEER_QTYS = {'half-beer': 0.5, 'full beer': 1}
BEER_PLACES = USER_DATA[USER_DATA['PLACE'].notnull()]['PLACE'].sort_values(ascending=True).unique()


def initialize_session_state():
    if 'beer_names' not in st.session_state:
        st.session_state['beer_names'] = BEER_NAMES

    if 'beer_places' not in st.session_state:
        st.session_state['beer_places'] = BEER_PLACES
