# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## MVP Predictions

            Predict who the BBWAA selected for league MVP for any year since the award was established.

            Note: This model only predicts position players. Pitchers may win the award; however, this model does not consider pitchers.

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown('#### Season'),
        dcc.Dropdown(
            id='season-drop',
            options=[
                {'label': '1948', 'value': 1948},
                {'label': '1949', 'value': 1949},
                {'label': '1950', 'value': 1950},
                {'label': '1951', 'value': 1951},
                {'label': '1952', 'value': 1952},
                {'label': '1953', 'value': 1953},
                {'label': '1954', 'value': 1954},
                {'label': '1955', 'value': 1955},
                {'label': '1956', 'value': 1956},
                {'label': '1957', 'value': 1957},
                {'label': '1958', 'value': 1958},
                {'label': '1997', 'value': 1997},
                {'label': '1998', 'value': 1998},
                {'label': '1999', 'value': 1999},
            ],
            value=1999
        ),
        dcc.Markdown('#### League'),
        dcc.Dropdown(
            id='league-drop',
            options=[
                {'label': 'American', 'value': 'American'},
                {'label': 'National', 'value': 'National'}
            ],
            value='National'
        ),   

    ]
)

column3 = dbc.Col(
    [
        dcc.Markdown('#### Timeframe'),
        dcc.Dropdown(
            id='timeframe-drop',
            options=[
                {'label': '7 Years', 'value': 7},
                {'label': '10 Years', 'value': 10},
                {'label': '15 Years', 'value': 15},
                {'label': '25 Years', 'value': 25},
                {'label': '50 Years', 'value': 50},
                {'label': 'Full', 'value': 88}
            ],
            value=10
        ),
        dcc.Markdown('#### Number of Results'),
        dcc.Dropdown(
            id='results-drop',
            options=[
                {'label': '1', 'value': 1},
                {'label': '3', 'value': 3},
                {'label': '5', 'value': 5},
                {'label': '10', 'value': 10}
            ],
            value=1
        ),
    ],
    md=3
)

column4 = dbc.Col(
    [
        html.H2('MVP Probability', className='mb-5'), 
        html.Div(id='pred-content', className='lead')
    ],
    md=3
)

import pandas as pd
merged_df = pd.read_csv('assets/final_df.csv')

@app.callback(
    Output('pred-content', 'children'),
    [Input('season-drop', 'value'), Input('league-drop', 'value'), Input('timeframe-drop', 'value'), Input('results-drop', 'value')]
)
def MVP_Prediction(season, league, timeframe=10, results=3):
    target = 'MVP'
    features = merged_df.drop(columns=[target, 'Player', 'Position', 
                                       'playerid']).columns

    test = merged_df[(merged_df.Season == season) & 
                     (merged_df.League == league)]
    train = merged_df[(merged_df.Season >= (season - timeframe)) & 
                       (merged_df.Season < season) & 
                      (merged_df.League == league)]
                    
    X_train = train[features]
    y_train = train[target]
    X_test = test[features]
    y_test = test[target]
    
    from sklearn.impute import SimpleImputer
    import category_encoders as ce
    from sklearn.pipeline import make_pipeline
    from sklearn.ensemble import RandomForestClassifier

    pipeline = make_pipeline(
        ce.OrdinalEncoder(),
        SimpleImputer(strategy='median'),
        RandomForestClassifier(n_estimators=100, random_state=99)
    )
    pipeline.fit(X_train, y_train)
    pred = pipeline.predict_proba(X_test)[:,1]

    player = test['Player']
    team = test['Team']

    pred_df = pd.DataFrame({'Player' : player, 
                            'Team' : team, 'Probability': (pred / pred.sum())})
    print(f'Top {results} Predictions for {season} {league} League MVP')
    pred_df.sort_values(by='Probability', ascending=False, inplace=True)

    number = pred_df.iloc[0][0]
    number2 = pred_df.iloc[0][2]

    return f'Predicted Winner is {number} with {number2:,.2%} probability'

layout = dbc.Row([column1, column2, column3, column4])