# -*- coding: utf-8 -*-
"""
@author: DieL
"""
import dash
from dash import dcc
from dash import html
import plotly.express as px

def grafico_barras(df, x, y, barra):
    app = dash.Dash(__name__)
    
    fig = px.bar(df, x, y, color=barra, barmode="group")

    app.layout = html.Div(children=[
        html.H1(children='Gráfico de minería'),

        html.Div(children='''
            En este gráfico encontramos la rentabilidad de la minería
            de los distintos minerales compactados, contando como base de calculo 
            el tiempo que se tarda en minar el mineral base y contrastandolo con 
            los minerales compactados. Orientado a los viejes y transporte.
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    app.run_server(debug=True)