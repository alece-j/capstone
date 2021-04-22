#inpsiration from https://github.com/nachi-hebbar/Forest-Fire-Prediction-Website

from flask import Flask, request, jsonify
from sutta_model import most_similar #Importing engine function
import pandas as pd
import numpy as np

app = Flask(__name__)

#Avoid switching the order of 'title' and 'confidence' keys
app.config['JSON_SORT_KEYS'] = False

df = pd.read_csv('./data/df_all_clean.csv')

with open('./data/pairwise_similarities.npy', 'rb') as f:
        pairwise_similarities = np.load(f)

#API endpoint
@app.route('/api/', methods=['POST'])
def process_request():

    #Parse received JSON request
    user_input = request.get_json(force=True)

    #Extract show title
    ref = user_input['ref']

    #Call recommendation engine
    recommended_suttas_dict = most_similar(ref, df, pairwise_similarities)

    return jsonify(recommended_suttas_dict)


if __name__ == '__main__':

    app.run()