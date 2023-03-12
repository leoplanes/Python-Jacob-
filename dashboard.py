from traitement_donnees import *
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import plotly.colors


#--------------------- Graphique des chiens qui mordent le plus (Quanti/Quali) -----------------------------------#

graph_1 = go.Figure([go.Bar(x=breed_name_counts['index'], y=breed_name_counts['count'])])

graph_1.update_layout(
    title='Races de chiens mordant le plus (Quanti/Quali)',
    xaxis_title='Races de chiens',
    yaxis_title='Nombre de morsures'
)

graph_1.update_traces(marker=dict(color=breed_name_counts['count'], colorbar=dict(title='Nombre de chiens'), colorscale='Viridis'))

"""graph_1.show()"""

#--------------------------------------------------------------------------------------------------------# 




#----------------------------------------- Graphique des morsures par mois (Quanti/Quali) -------------------------------# 

trace = go.Scatter(x=monthly_counts['index'], y=monthly_counts['count'], mode='lines+markers', marker=dict(size=8, color='blue'))
# graphique en lignes, avec des points pour chaque mois de l'année 

data = [trace]

layout = go.Layout(
    title='Nombre de morsures de chiens par mois (Quanti/Quali)',
    xaxis=dict(title='Mois'),
    yaxis=dict(title='Nombre de morsures')
)

graph_2 = go.Figure(data=data, layout=layout)

"""graph_2.show()"""  
#---------------------------------------------------------------------------------------#




#----------------------- Graphique des morsures par âge (Quanti/Quanti)  --------------------------------------#

color_scale = [[0, 'rgb(255,0,0)'], [0.5, 'rgb(255,255,0)'], [1, 'rgb(0,255,0)']]


graph_3 = px.scatter(morsures_par_age, x='age', y='count', size='count', color='age',
 color_continuous_scale=color_scale, size_max=60)

graph_3.update_layout(
    title='Nombre de morsures par âge de chien (Quanti/Quanti)',
    xaxis_title='Âge de chien',
    yaxis_title='Nombre de morsures'
)

graph_3.show()




#---------------------- Dashboard Streamlit ---------------------------# 

#met les données en cache pour améliorer les performances de l'application
"""
# Création du titre et de la description du tableau de bord
st.title("Tableau de bord - Chiens")
st.write("Description de votre tableau de bord")

# Affichage du premier graphique
st.plotly_chart(graph_1)

# Affichage du deuxième graphique
st.plotly_chart(graph_2)
"""





