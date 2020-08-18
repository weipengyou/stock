import os

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression
from yahoo_fin import stock_info as si


def get_last_stock_price(ticker):
    return si.get_data(ticker)


class Process_pipeline(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.lr = LinearRegression()

    def fit(self, X, Y=None):
        data = get_last_stock_price(X)
        df_features = create_features(data)
        df_features, Y = create_X_Y(df_features)
        self.lr.fit(df_features, Y)
        return self

    def transform(self, X, Y=None):
        data = get_last_stock_price(X)
        df_features = create_features(data)
        df_features, Y = create_X_Y(df_features)

        return self.lr.predict(df_features)


def create_features(df_stock, nlags=10):
    df_resampled = df_stock.resample('1D').mean()
    df_resampled = df_resampled[df_resampled.index.to_series().apply(lambda x: x.weekday() not in [5, 6])]
    lags_col_names = []
    for i in range(nlags + 1):
        df_resampled['lags_' + str(i)] = df_resampled['close'].shift(i)
        lags_col_names.append('lags_' + str(i))
    df = df_resampled[lags_col_names]
    df = df.dropna(axis=0)
    return df


def create_X_Y(df_lags):
    X = df_lags.drop('lags_0', axis=1)
    Y = df_lags[['lags_0']]
    return X, Y


class MyPredictor(object):
    def __init__(self, model):
        self._model = model

    def predict(self, instances, **kwargs):
        inputs = np.asarray(instances)
        return self.model.predict(inputs[0])

    @classmethod
    def from_path(cls, model_dir):
        model_path = os.path.join(model_dir, 'AAL.pkl')
        model = joblib.load(model_path)

        return cls(model)
