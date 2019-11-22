# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Do BBWAA writers vote in a predictable pattern?

            The Baseball Writers Association of America (BBWAA) votes annually on a number of Major League Baseball awards, the most prestigous being the league MVP.


            This app predicts the the probability of a player receiving the award.


            """
        ),
        dcc.Link(dbc.Button('Get Started', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
