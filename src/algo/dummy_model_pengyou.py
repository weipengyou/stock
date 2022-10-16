import logging

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression, LogisticRegression

def tagger(row):
    if row['next'] < row['lags_0']:
        return 'Sell'
    else:
        return 'Buy'

def create_features(df_stock, nlags=5):
    df_resampled = df_stock.copy()
    col_names = []
    for i in range(nlags):
        df_resampled['lags_' + str(i)] = df_resampled['close'].shift(i)
        col_names.append('lags_' + str(i))
    df_resampled['next'] = df_resampled['close'].shift(-1)
    df_resampled['out'] = df_resampled.apply(tagger, axis=1)
    df_resampled['ma10'] = df_resampled['close'].rolling(10).mean()
    df_resampled['month'] = df_resampled.index.month
    df_resampled['weekday'] = df_resampled.index.weekday
    col_names += ['ma10', 'month', 'weekday', 'out']
    df = df_resampled[col_names]
    print(df)
    df = df.dropna(axis=0)

    return df


def create_X_Y(df_clean):
    X = df_clean.drop('out', axis=1)
    Y = df_clean[['out']]
    return X, Y


class Stock_model(BaseEstimator, TransformerMixin):

    def __init__(self, data_fetcher):
        self.log = logging.getLogger()
        self.lr = LogisticRegression()
        self._data_fetcher = data_fetcher
        self.log.warning('here')

    def fit(self, X, Y=None):
        data = self._data_fetcher(X)
        df_features = create_features(data)
    #    print(df_features)
        df_features.drop(df_features.tail(1).index, inplace=True)
    #    print(df_features)
        df_features, Y = create_X_Y(df_features)
        self.lr.fit(df_features, Y)
        return self

    def predict(self, X, Y=None):
        print(X)
        data = self._data_fetcher(X, last=True)
        print(data)
        df_features = create_features(data)
        print(df_features)
        df_features, Y = create_X_Y(df_features)
        predictions = self.lr.predict(df_features)
        print(predictions)
        return predictions.flatten()[-1]
