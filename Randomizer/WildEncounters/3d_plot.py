# import plotly.express as px
# import pandas as pd
# spawners = pd.read_csv("spawners_merged_paldea.csv")
# spawners['X'] = 5000 - spawners['X'] # - For Paldea
# #spawners['X'] = 2000 - spawners['X'] # - For Kitakami/Blueberry
# fig = px.scatter_3d(spawners, x='X', y='Z', z='Y', color='area')
# fig.show()

import sympy as sp

# Define the variables
u1, u2, v1, v2, c = sp.symbols('u1 u2 v1 v2 c')

# Define the function F
def F(x1, x2):
    return sp.Matrix([x1 - 2*x2, x2, -x1 + x2])

# Check additivity
# Calculate F(u) + F(v)
F_u_plus_F_v = F(u1, u2) + F(v1, v2)
# Calculate F(u + v)
F_u_plus_v = F(u1 + v1, u2 + v2)
print(F_u_plus_F_v)
print(F_u_plus_v)

# Check homogeneity
# Calculate F(c*u)
F_c_times_u = F(c*u1, c*u2)
# Calculate c * F(u)
c_times_F_u = c * F(u1, u2)
print(c_times_F_u)
print(F_c_times_u)

# Verify if the properties hold
additivity_hold = F_u_plus_F_v == F_u_plus_v
homogeneity_hold = F_c_times_u == c_times_F_u


