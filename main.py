import config
import datetime

import pandas as pd
import streamlit as st


config.initialize_session_state()


st.title('Welcome to Hold My Beer')
st.subheader('The place where you count your beers')


def save_df_row_to_csv(
        csv_path: str,
        row_data: dict,
        row_type: str,
) -> pd.DataFrame:
    target_df = pd.read_csv(csv_path)
    df_row = pd.DataFrame(row_data)
    df = pd.concat([target_df, df_row], ignore_index=True)
    df.to_csv(csv_path, index=False)
    st.success(f'Saved {row_type}!')
    return df


def show_statistics():
    df = pd.read_csv(config.USER_DATA_PATH)
    st.subheader(f'Total nr of beers: {sum(df["QTY"]) + 152}')


beer_col, qty_col, place_col , description_col= st.columns(4)
beer_input, place_input = st.columns(2)
add_beer, add_place = st.columns(2)

beer_name = beer_col.selectbox('Select your beer', st.session_state.beer_names)
beer_qty = qty_col.selectbox('Select beer size', config.BEER_QTYS.keys())
description = description_col.text_input('Describe your experience')
beer_place = place_col.selectbox('Select place', st.session_state.beer_places)

if beer_name == '+ add beer':
    new_beer = st.text_input('Please enter beer name')
else:
    new_beer = beer_name

if beer_place == '+ add place':
    new_place = st.text_input('Please enter place name')
else:
    new_place = beer_place

if st.button('Count beer'):
    qty = config.BEER_QTYS[beer_qty]
    save_df_row_to_csv(
        csv_path=config.USER_DATA_PATH,
        row_data={
                    'BEER': [new_beer],
                    'QTY': [qty],
                    'USER': ['liviu'],
                    'PLACE': [new_place],
                    'DESCRIPTION': [description],
                    'DATETIME': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],

        },
        row_type='beer',
    )

st.subheader('Statistics')

if st.button('Refresh'):
    show_statistics()