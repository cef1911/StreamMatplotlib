import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# https://discuss.streamlit.io/t/how-to-draw-pie-chart-with-matplotlib-pyplot/13967/2
# https://discuss.streamlit.io/t/error-importing-matplotlib-pyplot-on-streamlit-server/28897/4

st.header('Demo of Histogram')

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

st.header('Demo of Pie Chart that will be used Kids Member Names, Team Names, Team Roles, and Fishing Results')

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
# st.snow()
