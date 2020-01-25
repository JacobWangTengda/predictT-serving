import pandas as pd
import pickle

def create_features(df, label=None):
    """
    Creates time series features from datetime index
    """
    df['date'] = df.index
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear
    
    X = df[['hour','dayofweek','quarter','month','year',
           'dayofyear','dayofmonth','weekofyear']]
    if label:
        y = df[label]
        return X, y
    
    return X

class output:
    def __init__(self, time, value):
        self.x = time
        self.y = value

def predict_timeseries(file, model_path):
    
    # read file
    df = pd.read_csv(file, index_col=[0], parse_dates=[0])
    label = df.columns[0]
    
    # load model
    model = pickle.load(open(model_path,"rb"))
    
    # create features
    X, y = create_features(df, label=label)
    print(y)
    
    # make prediction using loaded model
    fitted_y = model.predict(X)
    
    # create output object

    historical = output(df.index, y.tolist())
    fitted = output(df.index, list(fitted_y))

    
    return historical, fitted