# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

from joblib import load
import pandas as pd
final_df = pd.read_csv('assets/final_df.csv')

from app import app

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            """,  className='mb-5'
        ), 
        dcc.Markdown('#### Games'), 
        dcc.Dropdown(
            id='games', 
            options=[
                {'label': '162', 'value': 162},
                {'label': '150', 'value': 150},
                {'label': '140', 'value': 140},
                {'label': '130', 'value': 130},
                {'label': '50', 'value': 50}
                ],
            value=162,  
            className='mb-5', 
        ), 
        dcc.Markdown('#### Team'), 
        dcc.Dropdown(
            id = 'team', 
            options = [
                {'label': 'Angels', 'value': 'Angels'},
                {'label': 'Astros', 'value': 'Astros'},
                {'label': 'Atheltics', 'value': 'Athletics'},
                {'label': 'Blue Jays', 'value': 'Blue Jays'},
                {'label': 'Braves', 'value': 'Braves'},
                {'label': 'Brewers', 'value': 'Brewers'},
                {'label': 'Cardinals', 'value': 'Cardinals'},
                {'label': 'Cubs', 'value': 'Cubs'},
                {'label': 'Diamondbacks', 'value': 'Diamondbacks'},
                {'label': 'Dodgers', 'value': 'Dodgers'},
                {'label': 'Giants', 'value': 'Giants'},
                {'label': 'Indians', 'value': 'Indians'},
                {'label': 'Mariners', 'value': 'Mariners'},
                {'label': 'Marlins', 'value': 'Marlins'},
                {'label': 'Mets', 'value': 'Mets'},
                {'label': 'Nationals', 'value': 'Nationals'},
                {'label': 'Orioles', 'value': 'Orioles'},
                {'label': 'Padres', 'value': 'Padres'},
                {'label': 'Phillies', 'value': 'Phillies'},
                {'label': 'Pirates', 'value': 'Pirates'},
                {'label': 'Rangers', 'value': 'Rangers'},
                {'label': 'Rays', 'value': 'Rays'},
                {'label': 'Red Sox', 'value': 'Red Sox'},
                {'label': 'Reds', 'value': 'Reds'},
                {'label': 'Rockies', 'value': 'Rockies'},
                {'label': 'Royals', 'value': 'Royals'},
                {'label': 'Tigers', 'value': 'Tigers'},
                {'label': 'Twins', 'value': 'Twins'},
                {'label': 'White Sox', 'value': 'White Sox'},
                {'label': 'Yankees', 'value': 'Yankees'}, 
            ], 
            value = 'Yankees', 
            className='mb-5'
        ), 
    ],
    md=4,
)
column2 = dbc.Col(
    [
        
        dcc.Markdown('##### At Bats'),
        dcc.Dropdown(
            id='atbatst',
            options=[{'label': '500', 'value': 500}],
            value=500
        ),
        dcc.Markdown('##### Plate Appearances'),
        dcc.Dropdown(
            id='platest',
            options=[{'label': '600', 'value': 600}],
            value=600
        ),
        dcc.Markdown('##### Singles'),
        dcc.Dropdown(
            id='singlest',
            options=[{'label': '100', 'value': 70}],
            value=70
        ),
        dcc.Markdown('##### Walks'),
        dcc.Dropdown(
            id='bbst',
            options=[{'label': '100', 'value': 10}],
            value=10
        ),
        dcc.Markdown('##### Hit By Pitches'),
        dcc.Dropdown(
            id='hpbst',
            options=[{'label': '100', 'value': 11}],
            value=11
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='stealst',
            options=[{'label': '100', 'value': 106}],
            value=106
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='doublest',
            options=[{'label': '30', 'value': 30}],
            value=30
        ),
        dcc.Markdown('##### Triples'),
        dcc.Dropdown(
            id='triplest',
            options=[{'label': '50', 'value': 50},
                    {'label': '40', 'value': 40},
                    {'label': '10', 'value': 10},],
            value=40
        ),
        dcc.Markdown('##### Home Runs'),
        dcc.Dropdown(
            id='hrst',
            options=[{'label': '60', 'value': 60},
                    {'label': '50', 'value': 50},
                    {'label': '0', 'value': 0},],
            value=50
        ),
        dcc.Markdown('##### Runs'),
        dcc.Dropdown(
            id='runst',
            options=[{'label': '100', 'value': 106}],
            value=106
        ),
        dcc.Markdown('##### RBIs'),
        dcc.Dropdown(
            id='rbist',
            options=[{'label': '100', 'value': 106}],
            value=106
        ),
        dcc.Markdown('##### Caught Stealing'),
        dcc.Dropdown(
            id='caughtst',
            options=[{'label': '100', 'value': 100}],
            value=100
        ),
        dcc.Markdown('##### Strikeouts'),
        dcc.Dropdown(
            id='kst',
            options=[{'label': '100', 'value': 106}],
            value=106
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='wart',
            options=[{'label': '5', 'value': 5}],
            value=5
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='post',
            options=[{'label': 'Yes', 'value': 'Yes'},
                    {'label': 'No', 'value': 'No'},],
            value='Yes'
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='season',
            options=[{'label': '100', 'value': 2019}],
            value=2019
        ),
        dcc.Markdown('##### Stolen Bases'),
        dcc.Dropdown(
            id='name',
            options=[{'label': 'Ben', 'value': 'Ben'}],
            value='Ben'
        ),
    ]
)

column3 = dbc.Col(
    [
        html.H2('MVP Probability', className='mb-5'), 
        html.Div(id='predict-content', className='lead')
    ]
)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output('predict-content', 'children'),
    [Input('games', 'value'), Input('team', 'value'), Input('atbatst', 'value'),
    Input('platest', 'value'), Input('singlest', 'value'), Input('doublest', 'value'),
    Input('triplest', 'value')]
)
def User_Pred_FINAL(games, team, atbats, plates, singles, doubles, triples, hrs=25, runs=66, 
              rbis=55, bbs=17, hbps=1, ks=24, steals=7, caughts=2, war=2.4, postseason='No', season=2019, name='Boo'):
    import numpy as np
    
    key = {'Yankees': 'American', 'Blue Jays': 'American', 'Orioles': 'American', 'Red Sox': 'American',
             'Rays' : 'American', 'Tigers' : 'American', 'White Sox' : 'American', 'Indians': 'American', 
              'Twins' : 'American', 'Royals' : 'American', 'Astros' : 'American', 'Rangers' : 'American', 
             'Mariners' : 'American', 'Angels' : 'American', 'Athletics' : 'American', 'Braves' : 'National', 
             'Mets' : 'National', 'Marlins' : 'National', 'Nationals' : 'National', 'Phillies' : 'National', 
             'Reds' : 'National', 'Pirates' : 'National', 'Cardinals' : 'National', 'Cubs' : 'National', 
             'Brewers' : 'National', 'Dodgers' : 'National', 'Padres' : 'National', 'Rockies' : 'National', 
             'Giants' : 'National', 'Diamondbacks' : 'National'}
    league = key[team]
    
    hits = (singles)+doubles+triples+hrs
    avg = hits/atbats
    obp = (hits+bbs+hbps)/plates
    slg = (singles+(doubles*2)+(triples*3)+(hrs*4))/atbats
    ops = obp + slg
    
    sample_df = pd.DataFrame({'Season':season, 'Player': name, 'Team':team, 'G':games, 'AB':atbats,
                             'PA':plates, 'H':hits, '1B':singles, '2B':doubles, '3B':triples, 'HR':hrs,
                             'R':runs, 'RBI':rbis, 'BB':bbs, 'SO':ks, 'SB':steals, 'CS':caughts, 
                              'AVG':avg, 'OBP':obp, 'SLG':slg, 'OPS':ops, 'WAR':war, 'playerid':0, 
                              'League':league, 'Position': 'SS', 'Postseason':postseason, 'Season': season, 'MVP':np.NaN}, index=[0])
    
    quick = pd.concat([final_df, sample_df], sort=False)
    
    r_columns = ['H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'SB', 'AVG', 'SLG', 'OPS', 'WAR']

    for column in r_columns:
        sample_df[f'{column}_ranked'] = quick.groupby(['Season', 'League'])[column].rank(method='min', 
                                                                                         ascending=False).iloc[-1:]
        
    test_set = pd.concat([final_df[(final_df.Season == season) & (final_df.League == league)], sample_df], sort=False)


    features = final_df.drop(columns=['MVP', 'Player', 'Position', 
                                       'playerid', 'Team', 'WAR', 'WAR_ranked', 'Postseason']).columns

    test = test_set
    X_test = test[features]
    X_test_ready = X_test.iloc[:,1:]

    pred = pipeline.predict_proba(X_test_ready)[:,1]

    player_z = test['Player']
    team_z = test['Team']
    playerid_z = test['playerid']

    pred_df = pd.DataFrame({'id' : playerid_z, 'Player' : player_z, 
                            'Team' : team_z, 'Probability': (pred / pred.sum())})
    #return f'Prediction for {season} {league} League MVP'
    #return X_test_ready.shape
    
    number = pred_df[pred_df.id == 0].iloc[0][3]

    return f'Predicted probability is {number:,.2%}'