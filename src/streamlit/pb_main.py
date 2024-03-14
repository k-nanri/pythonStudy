import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("PB曲線グラフ")

data = [[0, 10, 2], [5, 4, 8]]
chart_data = pd.DataFrame(data=data, columns=["a", "b", "c"])
base = alt.Chart(chart_data).encode(x="a")
c = base.mark_line(color="red").encode(
    alt.Y("b", axis=alt.Axis(title="消化予定項目数"))
)
# d = base.mark_line().encode(y="c")
d = base.mark_line().encode(alt.Y("c", axis=alt.Axis(title="bug")))
e = (c + d).resolve_scale(y="independent")
st.altair_chart(e, use_container_width=True)
