import plotly.express as px
import pandas as pd
spawners = pd.read_csv("spawners_merged_paldea.csv")
spawners['X'] = 5000 - spawners['X']  # - For Paldea
# spawners['X'] = 2000 - spawners['X']  # - For Kitakami/Blueberry
fig = px.scatter_3d(spawners, x='X', y='Z', z='Y', color='area')
fig.show()


