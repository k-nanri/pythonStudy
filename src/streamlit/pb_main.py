import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("PB曲線グラフ")

data = [[10, 10, 2], [5, 5, 8]]
chart_data = pd.DataFrame(data=data, columns=["a", "b", "c"])
data = [[3, 4], [5, 4]]
bug = pd.DataFrame(data=data, columns=["a", "c"])
print(chart_data)

# c = alt.Chart(chart_data).mark_line().encode(x="a", y="b", tooltip=["a", "b"])
base = alt.Chart(chart_data).encode(x="a")
c = base.mark_line(color="red").encode(y="b")
d = base.mark_line().encode(y2="c")

st.altair_chart((c + d), use_container_width=True)
