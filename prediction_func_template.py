import os
import pandas as pd
import sys
from flask import Flask, request
import json
import pickle

# import config # runs logger config, must import before app initialized
from util import predict_timeseries
app = Flask(__name__)
# app.config.from_object(config.get_object())

# contruct the message including the results in JSON format to be put in the response
'''
historical: uploaded historical data
fitted: predictions on the history that the model makes based on the uploaded data
predicted: predictions on the future
'''
def _predict_message(historical, fitted):
    messagebody = {
        'historical': {
            'times': historical.x,
            'traffic': historical.y,
        },
        'fitted': {
            'times': fitted.x,
            'traffic': fitted.y,
        }
        # 'predicted': {
        #     'times': predictions.x,
        #     'traffic': predictions.y,
        # },
    }
    return messagebody


@app.route("/", methods=['POST'])
def predict():
    try:
        app.logger.debug(request.files)
        file = request.get_json()['file']
    except:
        info = sys.exc_info()
        app.logger.error('Raised Error\n\tType: %s\n\tValue: %s' % (info[0],info[1]))
        response = app.response_class(
            response='Method requires input data',
            status=500
        )
        return response
    
    try:
        # predict results
        historical, fitted = predict_timeseries(file, "model/model.pickle.dat")
        message_body = _predict_message(historical,fitted)

        # create response message
        response = app.response_class(
            response=json.dumps(message_body, default = str),
            mimetype='application/json'
        )
        return response
    
    except:
        info = sys.exc_info()
        app.logger.error('Raised Error\n\tType: %s\n\tValue: %s' % (info[0],info[1]))
        response = app.response_class(
            response='Server Error: Type=%s. Message=%s' % (info[0],info[1]),
            status=500
        )
        return response


# Only run server.py directly for developing/debugging. In prod run main.py
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)