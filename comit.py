from email.headerregistry import Address
from inspect import trace
from optparse import Values
from ssl import Options
from matplotlib import container
from sqlalchemy import create_engine
from venv import CORE_VENV_DEPS
from click import Option
from dash import html
from dash import dcc
import numpy as np
import matplotlib.pyplot as plt  
import mysql.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
#import dash_core_components as doc
#import dash_html_components as html
from dash.dependencies import Input, Output
app = dash.Dash(__name__)


#Db Change starts below:


db_connection_str = 'mysql+pymysql://root:root@localhost/mydatabase'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM my_med', con=db_connection)
df = df.groupby(['name', 'generic', 'form', 'strength', 'pharma'])[['price']].mean()
df.reset_index(inplace=True)
print(df[:6])



fig = px.bar(df, x="pharma", y="form", color="name", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Welcome to E.HealthCare'),

    html.Div(children='''
        Please Select the Medicine you want to order.
    '''),
    dcc.Dropdown(id="any_med",
                options=[
                    {"label": "1stCef", "value": "1stCef"},
                    {"label": "3-C", "value": "3-C"},
                    {"label": "3-Geocef", "value": "3-Geocef"},
                    {"label": "5X", "value": "5X"},
                    {"label": "A-B1", "value": "A-B1"},
                    {"label": "A-Cal", "value": "A-Cal"}],
                multi=False,
                value="1stCef",
                style={'width' : "40%"}
                ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)