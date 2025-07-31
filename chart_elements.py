import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.title("streamlit Charts Demo")

#generate Sample data
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)
st.subheader("the data")
st.write(chart_data)

#area chart
st.subheader("area chart")
st.area_chart(chart_data)

#bar chart
st.subheader("bar chart")
st.bar_chart(chart_data)

#line chart
st.subheader("line chart")
st.line_chart(chart_data)


#scatter chart
st.subheader("Scatter chart")
scatter_data = pd.DataFrame({
    'X' : np.random.randn(100),
    'Y' : np.random.randn(100)
})
st.scatter_chart(chart_data)

#map (displaying random points on a map)

st.subheader("map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

#pyplot
st.subheader("pyplot Chart")
fig, ax =plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)