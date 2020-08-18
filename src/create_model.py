# this script create a model and save it into a pickle file
from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline

from src.predictor import Process_pipeline

if __name__ == '__main__':
    pipe = make_pipeline(Process_pipeline())

    pipe.fit('AAL')
    with open('AAL.pkl', 'wb') as f:
        joblib.dump(pipe, f)
