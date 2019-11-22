# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

# Imports from this application
from app import app

from joblib import load


# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## MVP Predictions

            Every year the Baseball Writers Association of America (BBWAA) votes on Major League Baseball players to be awarded the Most Valuable Player (MVP) award. Two awards are given each season -- one for a player in the American League, one for a player in the National League. This award has been bestowed every year since 1931. I was able to retrieve a custom csv dataset from Fangraphs.com listing every season of every player since the award started. I started by eliminating seasons where a player had fewer than 400 plate appearances. In this dataset I chose to use features I thought to be important in the minds of BBWAA writers when selecting a player to vote for. MLB player stats have been at the forefront of sports statistics for a number of years and it would be inefficient to include so many of the numbers that the voters would either not be aware of or did not deem important enough to impact their voting. 
            
            """
        ),
        html.Img(src='assets/SHAP_IMG.png', className='img-fluid'),
        dcc.Markdown(
            """    

            Shown above is an example of a theoretical player in the 2019 season. This player played in the American league for the New York Yankees and has a 15% chance of winning the AL MVP. You can see that having 148 RBIs has a huge positive impact on his odds. The feature that has the most negative impact is Run Rank, as being only ranked 23rd is not ideal for a player trying to be considered the best.

            

            Along with a model that predicts probabilities for made-up player stats, I built one that attempts to predict the MVP winner for any given historical season. This model is based off of the same features, and uses training data from the 10 seasons leading up to the season chosen. This model was able to predict winners with accuracy that I was not expecting. The downside of this model, however, was that it was only able to use position player data and therefore could not predict a pitcher to be named MVP. This meant that in seasons where a pitcher was given the award, the model was unfortunately always wrong, regardless of its best efforts.  


            """
        ),
        dcc.Markdown("# Actual Outcome"),
        html.Img(src='assets/PIC.png', className='img-fluid'),
        dcc.Markdown('# Predicted Outcome'),
        html.Img(src='assets/PLEASE_WORK.jpg', className='img-fluid'),
        

    ],
    md=10
)

layout = dbc.Row([column1])