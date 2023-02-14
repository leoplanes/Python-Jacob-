from traitement_donnees import *
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

#--------------------- Graphique des chiens qui mordent le plus -----------------------------------#

data = {
    'breeds': ['Yorkshire Terrier', 'Shih Tzu', 'Chihuahua', 'Maltese', 'Labrador Retriever', 
               'American Pit Bull Mix / Pit Bull Mix', 'Labrador Retriever Crossbreed', 
               'American Pit Bull Terrier/Pit Bull', 'Havanese', 'Jack Russell Terrier'],
    'counts': [858, 839, 670, 519, 444, 379, 328, 311, 268, 255]
}

fig = go.Figure([go.Bar(x=data['breeds'], y=data['counts'])])

fig.update_layout(
    title='Races de chiens mordant le plus',
    xaxis_title='Races de chiens',
    yaxis_title='Nombre de morsures'
)

fig.update_traces(marker=dict(color=data['counts'], colorbar=dict(title='Nombre de chiens'), colorscale='Viridis'))

fig.show()

#--------------------------------------------------------------------------------------------------------# 