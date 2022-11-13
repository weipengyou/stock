from flask import Flask

from src.business_logic.process_query_pengyou import create_business_logic

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return f'Hello dear students, you should use a better route:!\nEX: get_stock_val/<ticker>\n'

@app.route('/hello/<variable>', methods=['GET'])
def hi(variable):
    val = variable*2
    return f'<HTML><HI>Hi {val}</HI></HTML>'




@app.route('/get_stock_val/<ticker>', methods=['GET'])
def get_stock_value(ticker):
    bl = create_business_logic()
    prediction = bl.do_predictions_for(ticker)

    return prediction
    #return f'Prediction for ticker {ticker} is {prediction}\n'


if __name__ == '__main__':
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='localhost', port=8080, debug=True)
