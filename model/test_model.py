import pandas as pd
final_df = pd.read_csv('C:/Users/Jordan Heuer/MVP-Prediction/assets/final_df.csv')

def MVP_Prediction(season, league, timeframe=10, results=3):
    target = 'MVP'
    features = final_df.drop(columns=[target, 'Player', 'Position', 
                                       'playerid']).columns

    test = final_df[(final_df.Season == season) & 
                     (final_df.League == league)]
    train = final_df[(final_df.Season >= (season - timeframe)) & 
                       (final_df.Season < season) & 
                      (final_df.League == league)]
                    
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
    return pred_df.sort_values(by='Probability', 
                               ascending=False).reset_index(
        drop=True)[:results].style.format({'Probability':"{:.0%}", 'Test Probability':"{:.1%}"})

MVP_Prediction(2018, 'American', timeframe=10, results=5)