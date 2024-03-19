import streamlit as st
import pandas as pd
import altair as alt

st.title("PB曲線グラフ")


chart_data = pd.read_csv("./data.csv")

base = alt.Chart(chart_data).encode(x="date:T")
remaning_test_items = base.mark_line(color="red").encode(
    alt.Y("残項目数", axis=alt.Axis(title="残項目数"))
)

bugs = base.mark_line().encode(alt.Y("バグ数", axis=alt.Axis(title="バグ数")))

pb_chart = alt.layer(remaning_test_items, bugs).resolve_scale(y="independent")
st.altair_chart(pb_chart, use_container_width=True)
