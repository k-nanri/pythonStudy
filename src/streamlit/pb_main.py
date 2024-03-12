import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("PB曲線グラフ")

data = [[10, 10], [5, 5]]
chart_data = pd.DataFrame(data=data, columns=["a", "b"])
print(chart_data)

c = alt.Chart(chart_data).mark_line().encode(x="a", y="b", tooltip=["a", "b"])

st.altair_chart(c, use_container_width=True)
