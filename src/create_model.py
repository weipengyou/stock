
# this script create a model and save it into a pickle file
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from yahoo_fin import stock_info as si
from sklearn.pipeline import make_pipeline
import pandas as pd
import joblib
def get_last_stock_price(ticker):

    return si.get_data(ticker)

class Process_pipeline(BaseEstimator,TransformerMixin):
    def __init__(self):
        self.lr = LinearRegression()



    def fit(self, X, Y=None):
        data = get_last_stock_price(X)
        df_features = create_features(data)
        df_features, Y = create_X_Y(df_features)
        self.lr.fit(df_features, Y)
        return self

    def transform(self, X, Y = None):
        data = get_last_stock_price(X)
        df_features = create_features(data)
        df_features, Y = create_X_Y(df_features)

        return self.lr.predict(df_features)





def create_features(df_stock,nlags = 10):
    df_resampled = df_stock.resample('1D').mean()
    df_resampled = df_resampled[df_resampled.index.to_series().apply(lambda x: x.weekday() not in [5, 6])]
    lags_col_names = []
    for i in range(nlags+1):
        df_resampled[f'lags_{i}'] = df_resampled['close'].shift(i)
        lags_col_names.append(f'lags_{i}')
    df = df_resampled[lags_col_names]
    df = df.dropna(axis=0)
    return df

def create_X_Y(df_lags):
    X = df_lags.drop('lags_0',axis=1)
    Y = df_lags[['lags_0']]
    return X, Y


if __name__ == '__main__':

    pipe = make_pipeline(Process_pipeline())

    pipe.fit('AAL')
    with open('AAL.pkl','wb') as f:
        joblib.dump(pipe,f)




